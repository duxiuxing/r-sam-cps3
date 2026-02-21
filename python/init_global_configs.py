# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from roms_xml import RomsXML


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\cps3-temp"
        dir2 = "X:\\"
        LocalConfigs._export_to_directory = Path(dir1)

        LocalConfigs._retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs._seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        RomsXML()


if __name__ == "__main__":
    Init_Global_Configs()

    print(LocalConfigs.repository_directory())
    print(LocalConfigs.export_to_directory())
    print(LocalConfigs.retroarch_directory())
    print(LocalConfigs.seven_zip_exe_path())
