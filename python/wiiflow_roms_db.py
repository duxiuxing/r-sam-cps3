# -- coding: UTF-8 --

from wiiflow_rom import WiiFlow_Rom


class WiiFlow_RomsDB:
    __instance = None

    @staticmethod
    def instance():
        if WiiFlow_RomsDB.__instance is None:
            WiiFlow_RomsDB()
        return WiiFlow_RomsDB.__instance

    def __init__(self):
        WiiFlow_RomsDB.__instance = self
        self.__crc32_to_rom = {}

    def all_rom_crc32_values(self):
        return self.__crc32_to_rom.keys()

    def all_roms(self):
        return self.__crc32_to_rom.values()

    def rom_exist(self, rom_crc32):
        return rom_crc32 in self.__crc32_to_rom.keys()

    def add_rom(self, rom: WiiFlow_Rom):
        self.__crc32_to_rom[rom.crc32] = rom

    def query_rom(self, rom_crc32=None, rom_file_title=None):
        if rom_crc32 is not None:
            return self.__crc32_to_rom.get(rom_crc32)

        if rom_file_title is not None:
            for rom in self.all_roms():
                if rom.file_title == rom_file_title:
                    return rom

        return None
