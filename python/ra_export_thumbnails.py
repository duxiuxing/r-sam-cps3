# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo

from r_sam_roms import RSamRoms
from ra_export_roms import RA_ExportFakeRoms


class RA_ExportThumbnails:
    def __init__(
        self,
        lpl_file_name,
        rom_crc32_to_dst_rom_path,
        xml_file_name,
        label_in_xml,
        src_boxart_folder="boxart",
        src_snap_folder="snap",
        src_title_folder="title",
    ):
        self.lpl_file_name = lpl_file_name
        self.rom_crc32_to_dst_rom_path = rom_crc32_to_dst_rom_path
        self.xml_file_name = xml_file_name
        self.label_in_xml = label_in_xml
        self.src_boxart_folder = src_boxart_folder
        self.src_snap_folder = src_snap_folder
        self.src_title_folder = src_title_folder

    def run(self):
        r_sam_roms = RSamRoms.instance()

        xml_file_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"export-config\\{self.xml_file_name}",
        )

        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for rom_elem in root.findall("Rom"):
            rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
            rom_info = r_sam_roms.query_rom_info(rom_crc32)

            label = Helper.remove_region(rom_elem.get(self.label_in_xml))

            src_boxart_path = RSamRoms.compute_image_path(
                rom_info, self.src_boxart_folder
            )
            dst_boxart_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.lpl_file_name}\\Named_Boxarts\\{label}.png",
            )
            Helper.copy_file(src_boxart_path, dst_boxart_path)

            src_snap_path = RSamRoms.compute_image_path(rom_info, self.src_snap_folder)
            dst_snap_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.lpl_file_name}\\Named_Snaps\\{label}.png",
            )
            Helper.copy_file(src_snap_path, dst_snap_path)

            src_title_path = RSamRoms.compute_image_path(
                rom_info, self.src_title_folder
            )
            dst_title_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"RetroArch\\thumbnails\\{self.lpl_file_name}\\Named_Titles\\{label}.png",
            )
            Helper.copy_file(src_title_path, dst_title_path)


if __name__ == "__main__":
    export_roms = RA_ExportFakeRoms()
    export_roms.run()

    RA_ExportThumbnails(
        lpl_file_name=f"认真玩 - {ConsoleConfigs.zhcn_name()}游戏",
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml="zhcn",
        src_boxart_folder="disc",
    ).run()

    RA_ExportThumbnails(
        lpl_file_name=f"R-Sam - {ConsoleConfigs.en_name()} Games",
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml="en",
    ).run()
