# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from export_roms import ExportFakeRoms
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from wiiflow_plugins_data import WiiFlowPluginsData


class ExportSnapshotFiles:
    def __init__(self, rom_crc32_to_dst_rom_path):
        self.rom_crc32_to_dst_rom_path = rom_crc32_to_dst_rom_path

    def run(self):
        wiiflow_plugins_data = WiiFlowPluginsData.instance()
        plugin_name = ConsoleConfigs.wiiflow_plugin_name()

        dst_folder_path = os.path.join(
            LocalConfigs.export_root_folder_path(), f"wiiflow\\snapshots\\{plugin_name}"
        )
        if not Helper.verify_folder_exist_ex(dst_folder_path):
            return

        # 根据导出的 ROM 文件来拷贝对应的封面文件
        for rom_crc32, dst_rom_path in self.rom_crc32_to_dst_rom_path.items():
            game_info = wiiflow_plugins_data.query_game_info(rom_crc32=rom_crc32)
            if game_info is None:
                continue

            src_path = WiiFlowPluginsData.compute_snapshot_file_path(game_info)
            if not os.path.exists(src_path):
                print(f"无效的源文件：{src_path}")
                continue

            rom_name = os.path.basename(dst_rom_path)
            dst_path = os.path.join(
                dst_folder_path, f"{Helper.get_rom_title(rom_name)}.png"
            )
            Helper.copy_file_if_not_exist(src_path, dst_path)


if __name__ == "__main__":
    export_roms = ExportFakeRoms()
    export_roms.run()

    ExportSnapshotFiles(export_roms.rom_crc32_to_dst_rom_path).run()
