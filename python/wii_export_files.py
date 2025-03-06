# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from console_configs import ConsoleConfigs
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wii_export_meta_xml import Wii_ExportMetaXml


class Wii_ExportFiles:
    @staticmethod
    def default_config_file_name():
        return "wii-files.xml"

    def __init__(self):
        self.config_file_name = Wii_ExportFiles.default_config_file_name()

    def run(self):
        if self.config_file_name is None:
            print("Wii_ExportFiles 实例未指定 .config_file_name")
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

        for app_elem in root.findall("APP"):
            app_name = app_elem.get("name")
            app_folder_name = app_elem.get("folder-name")

            rom_title = app_folder_name
            if "rom-title" in app_elem.attrib:
                rom_title = app_elem.get("rom-title")

            if "icon" in app_elem.attrib:
                src_icon_path = os.path.join(src_root, app_elem.get("icon"))
                dst_icon_path = os.path.join(
                    dst_root, f"apps\\{app_folder_name}\\icon.png"
                )
                image = Image.open(src_icon_path).resize((128, 48))
                image.save(dst_icon_path, format="PNG")

            gen_meta_xml = False
            if (
                "gen-meta-xml" in app_elem.attrib
                and app_elem.get("gen-meta-xml").lower() == "true"
            ):
                gen_meta_xml = True

            if gen_meta_xml:
                Wii_ExportMetaXml(app_name, app_folder_name, rom_title).run()

            src_dir_path = os.path.join(src_root, "wii\\apps\\retroarch-wii\\info")
            dst_dir_path = os.path.join(dst_root, f"apps\\{app_folder_name}\\info")
            Helper.copy_directory(src_dir_path, dst_dir_path)

            src_dol_path = os.path.join(
                src_root,
                f"wii\\apps\\retroarch-wii\\{ConsoleConfigs.ra_configs().core_file()}",
            )
            dst_dol_path = os.path.join(
                dst_root,
                f"apps\\{app_folder_name}\\{ConsoleConfigs.ra_configs().core_file()}",
            )
            Helper.copy_file(src_path, dst_path)

            dst_dol_path = os.path.join(dst_root, f"apps\\{app_folder_name}\\boot.dol")
            Helper.copy_file(src_path, dst_path)

            for elem in app_elem.findall("Folder"):
                src_path = os.path.join(src_root, elem.get("src"))
                dst_path = os.path.join(dst_root, elem.get("dst"))
                Helper.copy_directory(src_path, dst_path)

            for elem in app_elem.findall("File"):
                src_path = os.path.join(src_root, elem.get("src"))
                dst_path = os.path.join(dst_root, elem.get("dst"))
                Helper.copy_file(src_path, dst_path)


if __name__ == "__main__":
    export_files = Wii_ExportFiles()
    export_files.run()
