# -- coding: UTF-8 --

from rom_info import RomInfo


class RomExportInfo:
    def __init__(self, rom_info):
        self.game_name = rom_info.game_name
        self.rom_crc32 = rom_info.rom_crc32
        self.rom_bytes = rom_info.rom_bytes
        self.rom_title = rom_info.rom_title
        self.en_title = rom_info.en_title
        self.zhcn_title = rom_info.zhcn_title
        self.src_path = None
        self.dst_path = None
