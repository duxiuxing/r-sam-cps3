# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from helper import Helper
from console_configs import ConsoleConfigs
from local_configs import LocalConfigs
from rom_info import RomInfo


class LocalRoms:
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
        # 以下两个字典的内容都来自 roms 文件夹里的各个 .xml
        # 设置操作都在 self.reset_rom_crc32_to_path_and_info() 里
        self.rom_crc32_to_path = {}  # rom_crc32 : rom_path
        self.rom_crc32_to_info = {}  # rom_crc32 : RomInfo

    def load_roms_xml(self, xml_path):
        if not os.path.exists(xml_path):
            return

        tree = ET.parse(xml_path)
        root = tree.getroot()
        rom_extension = ConsoleConfigs.rom_extension()

        for game_elem in root.findall("Game"):
            game_name = game_elem.get("name")
            game_folder_path = os.path.join(os.path.dirname(xml_path), game_name)

            for rom_elem in game_elem.findall("Rom"):
                rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
                rom_title = rom_elem.get("title")
                rom_path = os.path.join(game_folder_path, f"{rom_crc32}{rom_extension}")
                if not os.path.exists(rom_path):
                    print(f"Missing ROM : {rom_path}")
                    continue
                else:
                    self.rom_crc32_to_path[rom_crc32] = rom_path
                    self.rom_crc32_to_info[rom_crc32] = RomInfo(
                        game_name=game_name,
                        rom_crc32=rom_crc32,
                        rom_bytes=rom_elem.get("bytes"),
                        rom_title=rom_title,
                        en_title=rom_elem.get("en"),
                        zhcn_title=rom_elem.get("zhcn"),
                    )

    def reset_rom_crc32_to_path_and_info(self):
        # 本函数执行的操作如下：
        # 1. 清空 self.rom_crc32_to_path 和 self.rom_crc32_to_info
        # 2. 读取 roms 文件夹里的各个 .xml
        # 3. 重新设置 self.rom_crc32_to_path 和 self.rom_crc32_to_info
        self.rom_crc32_to_path.clear()
        self.rom_crc32_to_info.clear()

        if Helper.files_in_letter_folder():
            for letter in "#ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                xml_path = os.path.join(
                    LocalConfigs.repository_folder_path(),
                    "roms\\{letter}\\{letter}.xml",
                )
                self.load_roms_xml(xml_path)
        else:
            xml_path = os.path.join(
                LocalConfigs.repository_folder_path(), "roms\\roms.xml"
            )
            self.load_roms_xml(xml_path)

    def query_rom_path(self, rom_crc32):
        if len(self.rom_crc32_to_path) == 0:
            self.reset_rom_crc32_to_path_and_info()

        if rom_crc32 in self.rom_crc32_to_path.keys():
            return self.rom_crc32_to_path[rom_crc32]
        else:
            return None


if __name__ == "__main__":
    local_roms = LocalRoms()
    local_roms.query_rom_path("00000000")
