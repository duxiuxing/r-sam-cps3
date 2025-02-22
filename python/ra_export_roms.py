# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo

from r_sam_roms import RSamRoms


class RA_ExportRoms:
    def __init__(self):
        self.rom_list_file_name = "ra-rom-list.xml"
        self.rom_title_filter = None
        self.export_fake_rom = True
        self.__rom_crc32_to_dst_path = {}

    def rom_list_file_path(self):
        return os.path.join(
            LocalConfigs.repository_directory(),
            f"config\\{self.rom_list_file_name}",
        )

    def rom_crc32_to_dst_path_items(self):
        return self.__rom_crc32_to_dst_path.items()

    def rom_dst_path(self, rom_crc32):
        return self.__rom_crc32_to_dst_path.get(rom_crc32)

    def run(self):
        if self.rom_list_file_name is None:
            print("RA_ExportRoms 实例未指定 rom_list_file_name")
            return False

        # 本函数执行的操作如下：
        # 1. 读取 self.rom_list_file_name，目前只需要根据 <Rom> 中的 crc32 和 title 就可以完成导出
        # 2. 根据 rom_crc32 在 RSamRoms 中查询对应的 rom_info
        # 3. 根据 rom_info 拼接出 src_path 和 dst_path
        # 4. 将 src_path 复制到 dst_path，如果目标文件已经存在会跳过
        r_sam_roms = RSamRoms.instance()

        xml_file_path = self.rom_list_file_path()
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效的文件 {xml_file_path}")
            return False

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        dst_roms_folder_path = os.path.join(
            LocalConfigs.root_directory_export_to(),
            f"Games\\{ConsoleConfigs.current_ra_core_configs().core_display_name()}",
        )
        if "dst_folder" in root.attrib:
            dst_roms_folder_path = os.path.join(
                LocalConfigs.root_directory_export_to(), root.get("dst_folder")
            )

        if not Helper.verify_exist_folder_ex(dst_roms_folder_path):
            print(f"【错误】无效的目标文件夹 {dst_roms_folder_path}")
            return False

        one_folder_one_rom = False
        if (
            "one_folder_one_rom" in root.attrib
            and root.get("one_folder_one_rom").lower() == "true"
        ):
            one_folder_one_rom = True

        self.__rom_crc32_to_dst_path = {}
        for rom_elem in root.findall("Rom"):
            rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
            rom_info = r_sam_roms.query_rom_info(rom_crc32)
            if rom_info is None:
                print(f"crc32 = {rom_crc32} 的 ROM 文件不存在")
                continue

            src_path = RSamRoms.compute_rom_path(rom_info)
            if not os.path.exists(src_path):
                print(f"【错误】无效的源文件 {src_path}")
                continue

            # 自定义标题在 self.rom_list_file_name 文件中配置的
            rom_title = rom_elem.get("title")
            if self.rom_title_filter is not None:
                if self.rom_title_filter != rom_title:
                    continue

            rom_name = rom_title + ConsoleConfigs.rom_extension()
            if one_folder_one_rom:
                # 把 ROM 文件放在以游戏命名的文件夹里
                rom_name = f"{rom_info.game_name}\\{rom_name}"

            dst_path = os.path.join(dst_roms_folder_path, rom_name)
            if Helper.verify_exist_folder_ex(os.path.dirname(dst_path)):
                self.__rom_crc32_to_dst_path[rom_crc32] = dst_path
                if self.export_fake_rom:
                    if not os.path.exists(dst_path):
                        open(dst_path, "w").close()
                else:
                    Helper.copy_file_if_not_exist(src_path, dst_path)

        if self.export_fake_rom:
            print(f"导出空的 ROM 文件到 {dst_roms_folder_path}")
        else:
            print(f"导出 ROM 文件到 {dst_roms_folder_path}")

        return True


if __name__ == "__main__":
    export_roms = RA_ExportRoms()
    export_roms.run()
