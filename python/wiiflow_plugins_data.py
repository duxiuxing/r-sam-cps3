# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from configparser import ConfigParser
from console_configs import ConsoleConfigs
from game_info import GameInfo
from game_tdb import GameTDB
from helper import Helper
from local_configs import LocalConfigs


class WiiFlowPluginsData(GameTDB):
    def __init__(self):

        # 机种对应的 WiiFlow 插件名称
        self.plugin_name = ConsoleConfigs.name()

        # game_id 为键，GameInfo 为值的字典
        # 内容来自 <self.plugin_name>.xml
        # 设置操作在 self.reset_game_id_to_info() 中实现
        self.game_id_to_info = {}

        # rom_crc32 为键，game_id 为值的字典
        # 内容来自 <self.plugin_name>.ini
        # 读取操作在 self.reset_rom_crc32_to_game_id() 中实现
        self.rom_crc32_to_game_id = {}

        # rom_title 为键，game_id 为值的字典
        # 内容来自 <self.plugin_name>.ini
        # 读取操作在 self.reset_rom_crc32_to_game_id() 中实现
        self.rom_title_to_game_id = {}

    def reset_game_id_to_info(self):
        # 本函数执行的操作如下：
        # 1. 读取 <self.plugin_name>.xml
        # 2. 重新设置 self.game_id_to_info

        xml_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wiiflow\\plugins_data\\{self.plugin_name}\\{self.plugin_name}.xml",
        )

        if not os.path.exists(xml_path):
            print(f"无效的文件：{xml_path}")
            return

        self.game_id_to_info.clear()
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for game_elem in root.findall("game"):
            game_name = game_elem.get("name")
            game_id = ""
            en_title = ""
            zhcn_title = ""
            for elem in game_elem:
                if elem.tag == "id":
                    game_id = elem.text
                elif elem.tag == "locale":
                    lang = elem.get("lang")
                    if lang == "EN":
                        en_title = elem.find("title").text
                        if en_title not in game_name.split(" / "):
                            print("英文名不一致")
                            print(f"\tname     = {game_name}")
                            print(f"\tEN title = {en_title}")
                    elif lang == "ZHCN":
                        zhcn_title = elem.find("title").text

            self.game_id_to_info[game_id] = GameInfo(
                id=game_id, name=game_name, en_title=en_title, zhcn_title=zhcn_title
            )

    def reset_rom_crc32_to_game_id(self):
        # 本函数执行的操作如下：
        # 1. 读取 <self.plugin_name>.ini
        # 2. 重新设置 self.rom_crc32_to_game_id 和 self.rom_title_to_game_id
        # 3. 同时设置 self.game_id_to_info 每个 GameInfo 的 rom_title

        ini_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"wii\\wiiflow\\plugins_data\\{self.plugin_name}\\{self.plugin_name}.ini",
        )

        if not os.path.exists(ini_path):
            print(f"无效的文件：{ini_path}")
            return

        self.rom_crc32_to_game_id.clear()
        self.rom_title_to_game_id.clear()

        ini_parser = ConfigParser()
        ini_parser.read(ini_path)
        if ini_parser.has_section(self.plugin_name):
            for rom_title in ini_parser[self.plugin_name]:
                values = ini_parser[self.plugin_name][rom_title].split("|")
                game_id = values[0]
                self.rom_title_to_game_id[rom_title] = game_id

                rom_crc32_list = set()
                for index in range(1, len(values) - 1):
                    rom_crc32 = values[index].rjust(8, "0")
                    rom_crc32_list.add(rom_crc32)
                    self.rom_crc32_to_game_id[rom_crc32] = game_id

                if game_id in self.game_id_to_info.keys():
                    self.game_id_to_info[game_id].rom_title = rom_title
                    self.game_id_to_info[game_id].rom_crc32_list = rom_crc32_list
                else:
                    print(f"game_id = {game_id} 不在 {self.plugin_name}.xml 中")

    def reset(self):
        # 重新从数据库文件中读取数据
        # 先读取 .xml 设置 self.game_id_to_info
        self.reset_game_id_to_info()

        # 再读取 .ini 设置 self.rom_crc32_to_game_id
        # 内部会设置 self.game_id_to_info 每个 GameInfo 的 rom_title
        self.reset_rom_crc32_to_game_id()

    def query_game_info(
        self, rom_crc32=None, rom_title=None, en_title=None, zhcn_title=None
    ):
        # GameTDB.query_game_info() 接口的实现

        # 防止重复读取
        if len(self.game_id_to_info) == 0:
            self.reset()

        game_id = None
        if rom_crc32 is not None:
            if rom_crc32 in self.rom_crc32_to_game_id.keys():
                game_id = self.rom_crc32_to_game_id.get(rom_crc32)
            else:
                print(f"{self.plugin_name}.ini 中未发现 {rom_crc32}")

        if game_id is None and rom_title is not None:
            if rom_title in self.rom_title_to_game_id.keys():
                game_id = self.rom_title_to_game_id.get(rom_title)
            else:
                print(f"{self.plugin_name}.ini 中未发现 {rom_title}")

        if game_id is not None and game_id in self.game_id_to_info.keys():
            return self.game_id_to_info.get(game_id)

        if en_title is None and zhcn_title is None:
            return None

        en_title_without_region = en_title
        if en_title is not None:
            en_title_without_region = Helper.remove_region(en_title)

        zhcn_title_without_region = zhcn_title
        if zhcn_title is not None:
            zhcn_title_without_region = Helper.remove_region(zhcn_title)

        for game_info in self.game_id_to_info.values():
            if en_title is not None:
                if (
                    game_info.en_title == en_title
                    or game_info.en_title == en_title_without_region
                ):
                    return game_info
            if zhcn_title is not None:
                if (
                    game_info.zhcn_title == zhcn_title
                    or game_info.zhcn_title == zhcn_title_without_region
                ):
                    return game_info

        print(f"{self.plugin_name}.xml 中未发现 {rom_title}")
        return None

    def export_all_fake_roms_to(self, dst_folder_path):
        # 防止重复读取
        if len(self.game_id_to_info) == 0:
            self.reset()

        for game_info in self.game_id_to_info.values():
            dst_path = os.path.join(
                dst_folder_path,
                f"{game_info.rom_title}{ConsoleConfigs.rom_extension()}",
            )
            if not os.path.exists(dst_path):
                open(dst_path, "w").close()


if __name__ == "__main__":
    plugin_name = ConsoleConfigs.name()
    plugins_data = WiiFlowPluginsData(plugin_name)
    dst_folder_path = os.path.join(
        f"{LocalConfigs.repository_folder_path()}-temp",
        f"roms\\Arcade\\{plugin_name}",
    )
    Helper.verify_folder_exist_ex(dst_folder_path)
    plugins_data.export_all_fake_roms_to(dst_folder_path)
