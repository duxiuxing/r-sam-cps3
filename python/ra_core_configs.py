# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from local_configs import LocalConfigs


class RA_CoreConfigs:
    def __init__(self, xml_file_name):
        self._items = {}
        xml_file_path = os.path.join(
            LocalConfigs.repository_directory(), f"config\\{xml_file_name}"
        )
        if not os.path.exists(xml_file_path):
            print(f"【错误】无效文件 {xml_file_path}")
        else:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for key, value in root.attrib.items():
                self._items[key] = value

    def _get_value(self, key, default_value=None):
        return self._items.get(key, default_value)

    def core_display_name(self):
        return self._get_value("core_display_name")

    def core_file_name_wii(self):
        return self._get_value("core_file_name_wii")

    def core_file_name_win(self):
        return self._get_value("core_file_name_win")


if __name__ == "__main__":
    ra_core_configs = RA_CoreConfigs("ra-core.xml")
    print(ra_core_configs.core_display_name())
    print(ra_core_configs.core_file_name_wii())
    print(ra_core_configs.core_file_name_win())
