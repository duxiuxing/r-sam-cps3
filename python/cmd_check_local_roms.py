# -- coding: UTF-8 --

import os

from cmd_handler import CmdHandler
from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_roms import LocalRoms
from rom_info import RomInfo
from wiiflow_plugins_data import WiiFlowPluginsData


class CmdCheckLocalRomsCrc32(CmdHandler):
    def __init__(self):
        super().__init__("Console - 检查 roms 文件夹里的 .xml 文件中的 rom_crc32")

    def run(self):
        LocalRoms().CheckRomsCrc32()


class CmdCheckLocalRomsTitles(CmdHandler):
    def __init__(self):
        super().__init__("Console - 检查 roms 文件夹里的 .xml 文件中的游戏名称")

    def run(self):
        # WiiFlowPluginsData 里有当前机种所有游戏的详细信息
        # 本函数用于检查 .xml 文件中的游戏名称是否与 WiiFlowPluginsData 里的一致
        wiiflow_plugins_data = WiiFlowPluginsData()
        plugin_name = wiiflow_plugins_data.plugin_name

        local_roms = LocalRoms()

        for rom_info in local_roms.rom_crc32_to_info.values():
            game_info = wiiflow_plugins_data.query_game_info(
                rom_crc32=rom_info.rom_crc32
            )
            if game_info is None:
                print(f"{plugin_name}.ini 中缺失配置")
                print(f"{rom_info.rom_title} = {rom_info.rom_crc32}")
            else:
                if rom_info.game_name != game_info.name:
                    print("游戏名称不一致")
                    print(f"\t{rom_info.game_name} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.name} 在 {plugin_name}.xml")

                if Helper.remove_region(rom_info.en_title) != game_info.en_title:
                    print(f"rom_crc = {rom_info.rom_crc32} 的 Rom 元素 en 属性不一致")
                    print(f"\t{rom_info.en_title} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.en_title} 在 {plugin_name}.xml")

                if Helper.remove_region(rom_info.zhcn_title) != game_info.zhcn_title:
                    print(f"rom_crc = {rom_info.rom_crc32} 的 Rom 元素 zhcn 属性不一致")
                    print(f"\t{rom_info.zhcn_title} 在 roms 文件夹里的 .xml 文件中")
                    print(f"\t{game_info.zhcn_title} 在 {plugin_name}.xml")


if __name__ == "__main__":
    CmdCheckLocalRomsCrc32().run()
    CmdCheckLocalRomsTitles().run()
