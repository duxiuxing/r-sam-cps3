# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from helper import Helper
from local_configs import LocalConfigs


class ExportFilesBase:
    def __init__(self):
        self.config_file_name = None

    def run(self):
        if self.config_file_name is None:
            print("ExportFilesBase 实例未指定 self.config_file_name")
            return

        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"export-config\\{self.config_file_name}",
        )

        if not os.path.exists(xml_file_path):
            print(f"【警告】无效的文件 {xml_file_path}")
            return

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        src_root = LocalConfigs.repository_directory()
        dst_root = LocalConfigs.root_directory_export_to()

        for elem in root.findall("Folder"):
            src_path = os.path.join(src_root, elem.get("src"))
            dst_path = os.path.join(dst_root, elem.get("dst"))
            Helper.copy_directory(src_path, dst_path)

        for elem in root.findall("File"):
            src_path = os.path.join(src_root, elem.get("src"))
            dst_path = os.path.join(dst_root, elem.get("dst"))
            Helper.copy_file(src_path, dst_path)
