# -- coding: UTF-8 --

import os

from common.local_configs import LocalConfigs


class WiiSdRomPathValue:
    def parse(self, rom_path):
        value = rom_path.replace(
            os.path.join(LocalConfigs.export_root_folder_path(), "Games"), "sd:\\Games"
        )
        return value.replace("\\", "/")
