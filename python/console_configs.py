# -- coding: UTF-8 --

import fnmatch


class ConsoleConfigs:
    @staticmethod
    def name():
        return "CPS3"

    @staticmethod
    def rom_extension():
        return ".zip"

    @staticmethod
    def rom_extension_match(file_name):
        return fnmatch.fnmatch(file_name, "*.zip")

    @staticmethod
    def rom_auto_rename():
        # 导入 ROM 文件的时候不自动重命名
        # 导出 ROM 文件的时候需要把 ROM 文件放在以游戏命名的文件夹里
        return False

    @staticmethod
    def default_core_name():
        return "Arcade (FB Alpha 2012 CPS-3)"
