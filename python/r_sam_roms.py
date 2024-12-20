# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from helper import Helper
from console_configs import ConsoleConfigs
from local_configs import LocalConfigs
from rom_info import RomInfo


class RSamRoms:
    @staticmethod
    def compute_rom_path(rom_info):
        # 根据 rom_info 拼接 ROM 文件的路径
        if Helper.files_in_letter_folder():
            letter = rom_info.game_name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"roms\\{letter}\\{rom_info.game_name}\\{rom_info.rom_crc32}{ConsoleConfigs.rom_extension()}",
            )
        else:
            return os.path.join(
                LocalConfigs.repository_folder_path(),
                f"roms\\{rom_info.game_name}\\{rom_info.rom_crc32}{ConsoleConfigs.rom_extension()}",
            )

    def __init__(self):
        # rom_crc32 为键，RomInfo 为值的字典
        # 内容来自 roms 文件夹里的各个 .xml
        self.rom_crc32_to_info = {}
        self.__load_rom_xml()

    def __load_xml_file(self, xml_file_path):
        if not os.path.exists(xml_file_path):
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        rom_extension = ConsoleConfigs.rom_extension()

        for game_elem in root.findall("Game"):
            game_name = game_elem.get("name")

            for rom_elem in game_elem.findall("Rom"):
                rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
                rom_info = RomInfo(
                    game_name=game_name,
                    rom_crc32=rom_crc32,
                    rom_bytes=rom_elem.get("bytes"),
                    rom_title=rom_elem.get("title"),
                    en_title=rom_elem.get("en"),
                    zhcn_title=rom_elem.get("zhcn"),
                )
                rom_path = RSamRoms.compute_rom_path(rom_info)
                if not os.path.exists(rom_path):
                    print(f"缺失 ROM 文件 {rom_path}")
                    continue
                else:
                    self.rom_crc32_to_info[rom_crc32] = rom_info

    def __load_rom_xml(self):
        # 本函数执行的操作如下：
        # 1. 读取 roms 文件夹里的各个 .xml
        # 2. 设置 self.rom_crc32_to_info
        if Helper.files_in_letter_folder():
            for letter in "#ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                xml_file_path = os.path.join(
                    LocalConfigs.repository_folder_path(),
                    "roms\\{letter}\\{letter}.xml",
                )
                self.__load_xml_file(xml_file_path)
        else:
            xml_file_path = os.path.join(
                LocalConfigs.repository_folder_path(), "roms\\roms.xml"
            )
            self.__load_xml_file(xml_file_path)

    def rom_exist(self, rom_crc32):
        return rom_crc32 in self.rom_crc32_to_info.keys()

    def query_rom_info(self, rom_crc32):
        if self.rom_exist(rom_crc32):
            return self.rom_crc32_to_info[rom_crc32]
        else:
            return None

    def add_rom_info(self, rom_crc32, rom_info):
        self.rom_crc32_to_info[rom_crc32] = rom_info

    def CheckRomsCrc32(self):
        # 检查 roms 文件夹里配置的 CRC32 是否等于实际值
        for rom_crc32, rom_info in self.rom_crc32_to_info.items():
            rom_path = RSamRoms.compute_rom_path(rom_info)
            rom_crc32_compute = Helper.compute_crc32(rom_path)
            if rom_crc32 != rom_crc32_compute:
                print(f"crc32 属性不一致 {rom_path}")
                print(f"\t{rom_crc32} 在 roms 文件夹里的 .xml 文件中")
                print(f"\t{rom_crc32_compute} 是实际计算出来的 crc32")
            rom_bytes_compute = str(os.stat(rom_path).st_size)
            if rom_info.rom_bytes != rom_bytes_compute:
                print(f"bytes 属性不一致 {rom_path}")
                print(f"\t{rom_info.rom_bytes} 在 roms 文件夹里的 .xml 文件中")
                print(f"\t{rom_bytes_compute} 是实际计算出来的文件大小")


if __name__ == "__main__":
    r_sam_roms = RSamRoms()
    r_sam_roms.query_rom_info("00000000")
