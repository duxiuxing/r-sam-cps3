# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase


class RA_ExportRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="roms-export.xml",
            dst_roms_folder_name=ConsoleConfigs.retroarch_default_core_name(),
            export_fake_roms=False,
        )


class RA_ExportFakeRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="roms-export.xml",
            dst_roms_folder_name=ConsoleConfigs.retroarch_default_core_name(),
            export_fake_roms=True,
        )


if __name__ == "__main__":
    RA_ExportFakeRoms().run()
