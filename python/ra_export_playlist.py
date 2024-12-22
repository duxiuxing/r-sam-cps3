# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo


class RA_ExportPlaylist:
    def __init__(
        self, lpl_file_name, rom_crc32_to_dst_rom_path, xml_file_name, label_in_xml
    ):
        self.lpl_file_name = lpl_file_name
        self.rom_crc32_to_dst_rom_path = rom_crc32_to_dst_rom_path
        self.xml_file_name = xml_file_name
        self.label_in_xml = label_in_xml

    def __write_header(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write('  "default_core_path": "",\n')
        lpl_file.write('  "default_core_name": "",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')

    def __write_footer(self, lpl_file):
        lpl_file.write("\n  ]\n")
        lpl_file.write("}")

    def export_assets_xmb_monochrome_png(self):
        src_playlist = os.path.join(
            LocalConfigs.repository_folder_path(),
            "image\\playlist\\playlist.png",
        )
        dst_playlist = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\assets\\xmb\\monochrome\\png\\{self.lpl_file_name}.png",
        )
        Helper.copy_file(src_playlist, dst_playlist)

        src_playlist_content = os.path.join(
            LocalConfigs.repository_folder_path(),
            "image\\playlist\\playlist-content.png",
        )
        dst_playlist_content = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\assets\\xmb\\monochrome\\png\\{self.lpl_file_name}-content.png",
        )
        Helper.copy_file(src_playlist_content, dst_playlist_content)

    def run(self):
        self.export_assets_xmb_monochrome_png()

        xml_file_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"export-config\\{self.xml_file_name}",
        )

        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        lpl_file_path = os.path.join(
            LocalConfigs.export_root_folder_path(),
            f"RetroArch\\playlists\\{self.lpl_file_name}.lpl",
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
                path = self.rom_crc32_to_dst_rom_path[rom_crc32].replace("\\", "\\\\")
                lpl_file.write(f'      "path": "{path}",\n')
                label = Helper.remove_region(rom_elem.get(self.label_in_xml))
                lpl_file.write(f'      "label": "{label}",\n')
                lpl_file.write('      "core_path": "DETECT",\n')
                lpl_file.write('      "core_name": "DETECT",\n')
                lpl_file.write(f'      "crc32": "{rom_crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{self.lpl_file_name}.lpl"\n')
                lpl_file.write("    }")

            self.__write_footer(lpl_file)
            lpl_file.close()
