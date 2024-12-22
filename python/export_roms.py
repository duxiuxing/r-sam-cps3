# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from common.console_configs import ConsoleConfigs
from common.helper import Helper
from common.local_configs import LocalConfigs
from common.rom_info import RomInfo

from r_sam_roms import RSamRoms


class ExportRomsBase:
    def __init__(
        self,
        xml_file_name,
        dst_roms_folder_name,
        export_fake_roms,
    ):
        self.rom_crc32_to_dst_rom_path = {}
        self.xml_file_name = xml_file_name
        self.dst_roms_folder_name = dst_roms_folder_name
        self.export_fake_roms = export_fake_roms

    def run(self):
        # 本函数执行的操作如下：
        # 1. 读取 self.roms_export_xml_file_name，目前只需要根据 <Rom> 中的 crc32 和 title 就可以完成导出
        # 2. 根据 rom_crc32 在 RSamRoms 中查询对应的 rom_info
        # 3. 根据 rom_info 拼接出 src_path 和 dst_path
        # 4. 将 src_path 复制到 dst_path，如果目标文件已经存在会跳过
        r_sam_roms = RSamRoms()

        xml_file_path = os.path.join(
            LocalConfigs.repository_folder_path(),
            f"export-config\\{self.xml_file_name}",
        )

        if not os.path.exists(xml_file_path):
            print(f"无效的文件：{xml_file_path}")
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for rom_elem in root.findall("Rom"):
            rom_crc32 = rom_elem.get("crc32").rjust(8, "0")
            rom_info = r_sam_roms.query_rom_info(rom_crc32)
            if rom_info is None:
                print(f"crc32 = {rom_crc32} 的 ROM 文件不存在")
                continue

            src_path = RSamRoms.compute_rom_path(rom_info)
            if not os.path.exists(src_path):
                print(f"无效的源文件：{src_path}")
                continue

            # 自定义标题在 self.roms_export_xml_file_name 文件中配置的
            rom_title_custom = rom_elem.get("title")
            rom_name = rom_title_custom + ConsoleConfigs.rom_extension()
            if ConsoleConfigs.rom_support_custom_title() is False:
                # 不支持 ROM 文件自定义命名的机种，导出时以 DB 中的命名为准
                # 而且需要把 ROM 文件放在以游戏命名的文件夹里
                rom_name = f"{rom_info.game_name}\\{rom_info.rom_title}{ConsoleConfigs.rom_extension()}"
                if rom_info.rom_title != rom_title_custom:
                    print("不支持 ROM 文件自定义命名")
                    print(f"rom_title_default = {rom_info.rom_title}")
                    print(f"rom_title_custom = {rom_title_custom}")

            dst_path = os.path.join(
                LocalConfigs.export_root_folder_path(),
                f"Games\\{self.dst_roms_folder_name}\\{rom_name}",
            )

            if Helper.verify_folder_exist_ex(os.path.dirname(dst_path)):
                self.rom_crc32_to_dst_rom_path[rom_crc32] = dst_path
                if self.export_fake_roms:
                    open(dst_path, "w").close()
                else:
                    Helper.copy_file_if_not_exist(src_path, dst_path)

        if self.export_fake_roms:
            print(f"导出空的 ROM 文件到 {self.dst_roms_folder_name}")
        else:
            print(f"导出 ROM 文件到 {self.dst_roms_folder_name}")


class ExportRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="roms-export.xml",
            dst_roms_folder_name=ConsoleConfigs.retroarch_default_core_name(),
            export_fake_roms=False,
        )


class ExportFakeRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="roms-export.xml",
            dst_roms_folder_name=ConsoleConfigs.retroarch_default_core_name(),
            export_fake_roms=True,
        )


if __name__ == "__main__":
    ExportFakeRoms().run()
