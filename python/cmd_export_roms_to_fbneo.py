# -- coding: UTF-8 --

from cmd_export_roms import CmdExportRoms
from console_configs import ConsoleConfigs


class CmdExportRomsToFBNeo(CmdExportRoms):
    def __init__(self):
        super().__init__(
            xml_file_name="roms-export-fbneo.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.name()}",
        )


if __name__ == "__main__":
    CmdExportRomsToFBNeo().run()
