# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from export_roms import ExportFakeRoms
from helper import Helper
from local_configs import LocalConfigs
from r_sam_roms import RSamRoms
from rom_info import RomInfo


class RetroArchPlaylist:
    def __init__(self, rom_crc32_to_dst_rom_path, xml_file_name, label_in_xml):
        self.rom_crc32_to_dst_rom_path = rom_crc32_to_dst_rom_path
        self.xml_file_name = xml_file_name
        self.label_in_xml = label_in_xml

    def __write_header(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write('  "default_core_path": "",\n')
        lpl_file.write('  "default_core_name": "",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 0,\n')
        lpl_file.write('  "left_thumbnail_mode": 0,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

    def __write_footer(self, lpl_file):
        lpl_file.write("\n  ]\n")
        lpl_file.write("}")

    def export(self, lpl_file_name):
        r_sam_roms = RSamRoms()

        xml_file_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"export-config\\{self.xml_file_name}",
        )

        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        lpl_file_path = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\playlists\\{lpl_file_name}.lpl",
        )

        if os.path.exists(lpl_file_path):
            os.remove(lpl_file_path)

        if not Helper.verify_folder_exist_ex(os.path.dirname(lpl_file_path)):
            return

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

            self.__write_header(lpl_file)

            first_rom = True

            for rom_elem in root.findall("Rom"):
                if first_rom:
                    first_rom = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
                lpl_file.write(
                    f'      "path": "{self.rom_crc32_to_dst_rom_path[rom_crc32]}",\n'
                )
                label = Helper.remove_region(rom_elem.get(self.label_in_xml))
                lpl_file.write(f'      "label": "{label}",\n')
                lpl_file.write('      "core_path": "DETECT",\n')
                lpl_file.write('      "core_name": "DETECT",\n')
                lpl_file.write(f'      "crc32": "{rom_crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{lpl_file_name}.lpl"\n')
                lpl_file.write("    }")

            self.__write_footer(lpl_file)
            lpl_file.close()


if __name__ == "__main__":
    export_roms = ExportFakeRoms()
    export_roms.run()

    RetroArchPlaylist(
        export_roms.rom_crc32_to_dst_rom_path, export_roms.xml_file_name, "zhcn"
    ).export(f"认真玩 - {ConsoleConfigs.zhcn_name()}游戏")

    RetroArchPlaylist(
        export_roms.rom_crc32_to_dst_rom_path, export_roms.xml_file_name, "en"
    ).export(f"R-Sam - {ConsoleConfigs.en_name()} Games")