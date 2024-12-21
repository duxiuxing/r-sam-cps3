# -- coding: UTF-8 --

from cmd_export_roms import CmdExportRomsBase
from console_configs import ConsoleConfigs


class CmdExportRomsToFBNeo(CmdExportRomsBase):
    def __init__(self):
        super().__init__(
            roms_export_xml_name="roms-export-fbneo.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=False,
        )


class CmdExportFakeRomsToFBNeo(CmdExportRomsBase):
    def __init__(self):
        super().__init__(
            roms_export_xml_name="roms-export-fbneo.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=True,
        )


if __name__ == "__main__":
    CmdExportFakeRomsToFBNeo().run()
