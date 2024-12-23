# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase


class RA_ExportFBNeoRoms(ExportRomsBase):
    @staticmethod
    def default_roms_export_xml():
        return "fbneo-roms-export.xml"

    @staticmethod
    def default_dst_folder_name():
        return f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}"

    def __init__(self):
        super().__init__()
        self.xml_file_name = RA_ExportFBNeoRoms.default_roms_export_xml()
        self.dst_folder_name = RA_ExportFBNeoRoms.default_dst_folder_name()
        self.export_fake_roms = False


class RA_ExportFakeFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__()
        self.xml_file_name = RA_ExportFBNeoRoms.default_roms_export_xml()
        self.dst_folder_name = RA_ExportFBNeoRoms.default_dst_folder_name()
        self.export_fake_roms = True


if __name__ == "__main__":
    export_roms = RA_ExportFakeFBNeoRoms()
    export_roms.run()
