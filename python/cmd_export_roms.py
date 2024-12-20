# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from cmd_handler import CmdHandler
from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from local_roms import LocalRoms
from rom_info import RomInfo
from wiiflow_plugins_data import WiiFlowPluginsData


class CmdExportRoms(CmdHandler):
    def __init__(
        self,
        xml_file_name="roms-export.xml",
        dst_roms_folder_name=ConsoleConfigs.default_core_name(),
    ):
        self.xml_file_name = xml_file_name
        self.dst_roms_folder_name = dst_roms_folder_name
        super().__init__(
            f"{ConsoleConfigs.name()} - 导出 ROM 文件到 {dst_roms_folder_name}"
        )

    def run(self):
        # 本函数执行的操作如下：
        # 1. 读取 roms-export.xml，目前只需要根据文件中的 rom_crc32 就可以完成导出
        # 2. 根据 rom_crc32 在 LocalRoms 中查询对应的 rom_info
        # 3. 根据 rom_info 拼接出 src_path 和 dst_path
        # 4. 将 src_path 复制到 dst_path，如果目标文件已经存在会跳过
        local_roms = LocalRoms()

        xml_path = os.path.join(
            LocalConfigs.repository_folder_path(), self.xml_file_name
        )

        if not os.path.exists(xml_path):
            print(f"无效的文件：{xml_path}")
            return

        tree = ET.parse(xml_path)
        root = tree.getroot()

        for game_elem in root.findall("Rom"):
            rom_crc32 = game_elem.get("crc32").rjust(8, "0")
            rom_info = local_roms.query_rom_info(rom_crc32)
            if rom_info is None:
                print(f"crc32 = {rom_crc32} 的 ROM 文件不存在")
                continue

            src_path = LocalRoms.compute_rom_path(rom_info)
            if not os.path.exists(src_path):
                print(f"无效的源文件：{src_path}")
                continue

            dst_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"Games\\{self.dst_roms_folder_name}\\{rom_info.game_name}\\{rom_info.rom_title}{ConsoleConfigs.rom_extension()}",
            )

            if Helper.verify_folder_exist_ex(os.path.dirname(dst_path)):
                Helper.copy_file_if_not_exist(src_path, dst_path)


if __name__ == "__main__":
    CmdExportRoms().run()
    CmdExportRoms(
        xml_file_name="roms-export-fbneo.xml",
        dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.name()}",
    ).run()
