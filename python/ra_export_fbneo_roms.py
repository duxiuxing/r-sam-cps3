# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase


class RA_ExportFBNeoRoms(ExportRomsBase):
    @staticmethod
    def default_config_file_name():
        return "ra-fbneo-roms.xml"

    def __init__(self):
        super().__init__()
        self.config_file_name = RA_ExportFBNeoRoms.default_config_file_name()
        self.export_fake_roms = False


class RA_ExportFakeFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__()
        self.config_file_name = RA_ExportFBNeoRoms.default_config_file_name()
        self.export_fake_roms = True


if __name__ == "__main__":
    export_roms = RA_ExportFakeFBNeoRoms()
    export_roms.run()
