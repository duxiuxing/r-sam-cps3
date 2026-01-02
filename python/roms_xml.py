# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB


class RomsXML:
    @staticmethod
    def __parse(xml_file_path: Path):
        if not xml_file_path.exists():
            return

        game_list_elem = ET.parse(xml_file_path).getroot()

        for game_elem in game_list_elem.findall("Game"):
            game = Game(id=game_elem.get("id"), en_title=game_elem.get("en_title"))
            game.zhcn_title = game_elem.get("zhcn_title")
            GamesDB.instance().add_game(game)

            for rom_elem in game_elem.findall("Rom"):
                parent_rom = RomsDB.instance().query_rom(
                    rom_crc32=rom_elem.get("parent_rom_crc32"),
                    rom_file_name=rom_elem.get("parent_rom_file"),
                )
                rom = Rom(
                    game_id=game.id,
                    crc32=rom_elem.get("crc32").rjust(8, "0"),
                    bytes=rom_elem.get("bytes"),
                    file_name=rom_elem.get("file_name"),
                    parent_rom=parent_rom,
                    en_title=rom_elem.get("en_title"),
                    zhcn_title=game_elem.get("zhcn_title"),
                )
                RomsDB.instance().add_rom(rom)
                game.rom_list.append(rom)

                rom_path = ResourceFileHelper.compute_rom_path(rom)
                if rom_path is None:
                    print(f"【错误】缺失 ROM 文件 {rom.file_name}")
                elif not rom_path.exists():
                    print(f"【错误】缺失 ROM 文件 {rom_path}")

    @staticmethod
    def load():
        # 本函数执行的操作如下：
        # 1. 读取 roms 文件夹里的各个 .xml 文件
        # 2. 构建 GamesDB 和 RomsDB
        repository_dir = Path(LocalConfigs.repository_directory())
        if Helper.files_in_letter_folder():
            for letter in "#ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                xml_file_path = repository_dir.joinpath(f"roms\\{letter}\\{letter}.xml")
                RomsXML.__parse(xml_file_path)
        else:
            xml_file_path = repository_dir.joinpath("roms\\roms.xml")
            RomsXML.__parse(xml_file_path)


if __name__ == "__main__":
    RomsXML.load()
