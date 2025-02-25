# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from console_configs import ConsoleConfigs
from ra_core_info import RA_CoreInfo


class PlaylistHeaderBase(ABC):
    @abstractmethod
    def write(self, lpl_file):
        pass


class BlankPlaylistHeader(PlaylistHeaderBase):
    def write(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write('  "default_core_path": "",\n')
        lpl_file.write('  "default_core_name": "",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')


class WiiSdPlaylistHeader(PlaylistHeaderBase):
    def __init__(self, app_folder_name):
        self._app_folder_name = app_folder_name

    def write(self, lpl_file):
        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(
            f'  "default_core_path": "sd:/apps/{self._app_folder_name}/{ConsoleConfigs.ra_default_core_file_title()}_wii.dol",\n'
        )
        lpl_file.write(
            f'  "default_core_name": "{ConsoleConfigs.current_ra_core_info().core_display_name}",\n'
        )
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 3,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')
