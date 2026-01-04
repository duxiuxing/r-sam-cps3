# -- coding: UTF-8 --

import json

from local_configs import LocalConfigs
from pathlib import Path
from ra_rom import RA_Rom


class RA_PlaylistImport:
    @staticmethod
    def parse(lpl_file_path: Path):
        with open(lpl_file_path, "r") as file:
            items = json.load(file)["items"]
            for item in items:
                rom = RA_Rom(
                    file_path=Path(item["path"]),
                    label=item["label"],
                    crc32=item["crc32"].split("|")[0],
                    playlist_name=Path(item["db_name"]).name,
                )

    @staticmethod
    def try_playlist_png_file(playlist_name):
        pass
    
    @staticmethod
    def __try_rom_file(rom: RA_Rom):
        pass

    @staticmethod
    def __try_thumbnail_file(rom: RA_Rom, src_folder_name, dst_folder_name):
        pass


if __name__ == "__main__":
    RA_PlaylistImport.try_playlist_png_file(RA_Configs.playlist_name())
    lpl_file_path = Path("X:\\RetroArch-Win64\\playlists\\FBNeo - Arcade Games.lpl")
    RA_PlaylistImport.parse(lpl_file_path)
