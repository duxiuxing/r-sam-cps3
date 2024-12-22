# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase


class RA_ExportFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=False,
        )


class RA_ExportFakeFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=True,
        )


if __name__ == "__main__":
    RA_ExportFakeFBNeoRoms().run()
