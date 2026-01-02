# -- coding: UTF-8 --

from rom import Rom


class RomsDB:
    __instance = None

    @staticmethod
    def instance():
        if RomsDB.__instance is None:
            RomsDB()
        return RomsDB.__instance

    def __init__(self):
        RomsDB.__instance = self
        self.__crc32_to_rom = {}

    def rom_exist(self, rom_crc32):
        return rom_crc32 in self.__crc32_to_rom.keys()

    def add_rom(self, rom: Rom):
        self.__crc32_to_rom[rom.crc32] = rom

    def query_rom(self, rom_crc32=None, rom_file_name=None):
        if rom_crc32 is not None:
            return self.__crc32_to_rom.get(rom_crc32)

        if rom_file_name is not None:
            for rom in self.__crc32_to_rom.values():
                if rom.file_name == rom_file_name:
                    return rom

        return None
