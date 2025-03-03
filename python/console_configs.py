# -- coding: UTF-8 --

import fnmatch
import os
import xml.etree.ElementTree as ET

from local_configs import LocalConfigs
from ra_core_configs import RA_CoreConfigs


class ConsoleConfigs:
    __instance = None

    def __init__(self):
        if ConsoleConfigs.__instance is not None:
            raise Exception("请使用 ConsoleConfigs._instance() 获取实例")
        else:
            ConsoleConfigs.__instance = self

        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(), "config\\console.xml"
        )
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效文件 {xml_file_path}")
        else:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            self._ra_core_configs = RA_CoreConfigs(root.attrib["ra_core_configs"])
            self._rom_extension = root.attrib["rom_extension"]
            self._wiiflow_plugin_name = root.attrib["wiiflow_plugin_name"]

    @staticmethod
    def _instance():
        # 获取单例实例
        if ConsoleConfigs.__instance is None:
            ConsoleConfigs()
        return ConsoleConfigs.__instance

    @staticmethod
    def rom_extension():
        # ROM 文件的扩展名
        return ConsoleConfigs._instance()._rom_extension

    @staticmethod
    def rom_extension_match(file_name):
        pat = f"*{ConsoleConfigs.rom_extension()}"
        return fnmatch.fnmatch(file_name, pat)

    @staticmethod
    def current_ra_core_configs():
        # RetroArch 核心信息
        return ConsoleConfigs._instance()._ra_core_configs

    @staticmethod
    def set_ra_core_configs(ra_core_configs):
        ConsoleConfigs._instance()._ra_core_configs = ra_core_configs

    @staticmethod
    def wiiflow_plugin_name():
        # WiiFlow 的插件名称
        return ConsoleConfigs._instance()._wiiflow_plugin_name


if __name__ == "__main__":
    print(ConsoleConfigs.rom_extension())
    file_name = "test.zip"
    if ConsoleConfigs.rom_extension_match(file_name):
        print(f"{file_name} ROM 文件名匹配成功")
    else:
        print(f"{file_name} ROM 文件名不匹配")
    print(ConsoleConfigs.current_ra_core_configs().core_display_name())
    print(ConsoleConfigs.wiiflow_plugin_name())
