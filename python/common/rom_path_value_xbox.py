# -- coding: UTF-8 --

import os

from common.local_configs import LocalConfigs


class XBoxRomPathValue:
    def parse(self, rom_path):
        value = rom_path.replace(
            os.path.join(LocalConfigs.export_root_folder_path(), "Games"), "E:\\Games"
        )
        return value.replace("\\", "\\\\")
