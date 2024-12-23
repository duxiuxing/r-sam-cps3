# -- coding: UTF-8 --


class WinRomPathValue:
    def parse(self, rom_path):
        return rom_path.replace("\\", "\\\\")
