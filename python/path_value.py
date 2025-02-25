# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from local_configs import LocalConfigs


class PathValueBase(ABC):
    @abstractmethod
    def parse(self, path):
        pass


# 把 Windows 路径转成 Android 路径
class AndroidPathValue(PathValueBase):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"),
            "/storage/emulated/0/Games",
        )
        return value.replace("\\", "/")


# 把 Windows 路径转成 Wii SD 路径
class WiiSdPathValue(PathValueBase):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"), "sd:\\Games"
        )
        return value.replace("\\", "/")


# RetraArch 要求 Windows 路径使用双反斜杠
class WinPathValue(PathValueBase):
    def parse(self, path):
        return path.replace("\\", "\\\\")


# 把 Windows 路径转成 XBOX 路径
class XBoxPathValue(PathValueBase):
    def parse(self, path):
        value = path.replace(
            os.path.join(LocalConfigs.root_directory_export_to(), "Games"), "E:\\Games"
        )
        return value.replace("\\", "\\\\")
