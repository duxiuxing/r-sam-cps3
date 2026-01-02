# -- coding: UTF-8 --

from pathlib import Path


class Rom:
    def __init__(
        self,
        game_id="",
        crc32="",
        bytes="",        
        file_name="",
        parent_rom=None,
        en_title="",
        zhcn_title="",
    ):
        self.game_id = game_id
        self.crc32 = crc32
        self.bytes = bytes

        self.file_name = Path(file_name).name
        self.file_title = Path(file_name).stem
        self.file_extension = Path(file_name).suffix
        
        self.parent_rom = parent_rom

        self.en_title = en_title
        self.zhcn_title = zhcn_title
