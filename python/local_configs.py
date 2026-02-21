# -- coding: UTF-8 --

import os
from pathlib import Path


class LocalConfigs:
    _repository_directory = Path(os.getcwd())

    @staticmethod
    def repository_directory():
        # 本地仓库路径
        return LocalConfigs._repository_directory

    _export_to_directory = None

    @staticmethod
    def export_to_directory():
        # 导出根目录路径
        if LocalConfigs._export_to_directory is None:
            dir0 = (
                "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
            )
            dir1 = "D:\\workspace\\github\\R-Sam-1980\\cps3-temp"
            dir2 = "X:\\"
            LocalConfigs._export_to_directory = Path(dir1)

        return LocalConfigs._export_to_directory

    @staticmethod
    def retroarch_directory():
        return Path("X:\\RetroArch-Win64")

    @staticmethod
    def seven_zip_exe_path():
        # 本机 7z.exe 的路径
        return Path("C:\Program Files\7-Zip\7z.exe")


if __name__ == "__main__":
    print(LocalConfigs.repository_directory())
    print(LocalConfigs.export_to_directory())
    print(LocalConfigs.retroarch_directory())
    print(LocalConfigs.seven_zip_exe_path())
