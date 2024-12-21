# -- coding: UTF-8 --

from export_roms import ExportRomsBase
from console_configs import ConsoleConfigs


class ExportFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=False,
        )


class ExportFakeFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=True,
        )


if __name__ == "__main__":
    ExportFakeFBNeoRoms().run()
