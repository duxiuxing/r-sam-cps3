# -- coding: UTF-8 --

import os
import shutil
import zlib

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from rom import Rom
from roms_db import RomsDB


class ResourceFileHelper:
    @staticmethod
    def compute_rom_path(rom: Rom):
        game = GamesDB.instance().query_game_by_id(rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())

        rom_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            rom_parent_dir = repository_dir.joinpath(f"roms\\{letter}")
        else:
            rom_parent_dir = repository_dir.joinpath("roms")

        rom_path = rom_parent_dir.joinpath(f"{rom.crc32}\\{rom.file_name}")
        if rom_path.exists() and rom_path.is_file():
            return rom_path

        rom_path = rom_parent_dir.joinpath(rom.file_name)
        if rom_path.exists() and rom_path.is_file():
            return rom_path

        return None

    @staticmethod
    def compute_media_path(rom: Rom, folder_name, file_extension):
        game = GamesDB.instance().get_game_by_id(rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())

        folder_path = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            folder_path = repository_dir.joinpath(f"media\\{folder_name}\\{letter}")
        else:
            folder_path = repository_dir.joinpath(f"media\\{folder_name}")

        image_path = folder_path.joinpath(f"{rom.file_title}{file_extension}")
        if image_path.exists() and image_path.is_file():
            return image_path

        image_path = folder_path.joinpath(f"{game.en_title}{file_extension}")
        if image_path.exists() and image_path.is_file():
            return image_path

        return None
