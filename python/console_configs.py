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
        return False
