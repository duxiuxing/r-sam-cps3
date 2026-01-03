# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from rom import Rom
from roms_db import RomsDB


class ResourceFileHelper:
    @staticmethod
    def compute_rom_file_path(rom: Rom, include_crc32: bool):
        game = GamesDB.instance().query_game(game_id=rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())

        rom_file_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            rom_file_parent_dir = repository_dir.joinpath(f"roms\\{letter}")
        else:
            rom_file_parent_dir = repository_dir.joinpath("roms")

        if include_crc32:
            return rom_file_parent_dir.joinpath(f"{rom.crc32}\\{rom.file_name}")
        else:
            return rom_file_parent_dir.joinpath(rom.file_name)

    @staticmethod
    def compute_media_file_path(
        rom: Rom, folder_name: str, file_extension: str, use_game_en_title: bool
    ):
        game = GamesDB.instance().get_game_by_id(rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())

        media_file_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            media_file_parent_dir = repository_dir.joinpath(
                f"media\\{folder_name}\\{letter}"
            )
        else:
            media_file_parent_dir = repository_dir.joinpath(f"media\\{folder_name}")

        if use_game_en_title:
            return media_file_parent_dir.joinpath(f"{game.en_title}{file_extension}")
        else:
            return media_file_parent_dir.joinpath(f"{rom.file_title}{file_extension}")
