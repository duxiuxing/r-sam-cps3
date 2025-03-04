# -- coding: UTF-8 --

import os

from abc import ABC, abstractmethod
from console_configs import ConsoleConfigs
from ra_configs import RA_Configs


class RA_PlaylistHeader(ABC):
    @staticmethod
    def create_instance():
        sys_code = ConsoleConfigs.ra_configs().sys_code()
        if sys_code == RA_Configs.SYS_WII:
            return Wii_PlaylistHeader()
        elif sys_code == RA_Configs.SYS_WIN:
            return Win_PlaylistHeader()
        else:
            return None

    @abstractmethod
    def write(self, lpl_file):
        pass


class Win_PlaylistHeader(RA_PlaylistHeader):
    def write(self, lpl_file):
        ra_configs = ConsoleConfigs.ra_configs()

        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(
            f'  "default_core_path": ".\\\\core\\\\{ra_configs.default_core_file()}",\n'
        )
        lpl_file.write(f'  "default_core_name": "{ra_configs.default_core_name()}",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 4,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')


class Wii_PlaylistHeader(RA_PlaylistHeader):
    def __init__(self, app_folder_name):
        self._app_folder_name = app_folder_name

    def write(self, lpl_file):
        ra_configs = ConsoleConfigs.ra_configs()

        lpl_file.write("{\n")
        lpl_file.write('  "version": "1.5",\n')
        lpl_file.write(
            f'  "default_core_path": "./{ra_configs.default_core_file()}",\n'
        )
        lpl_file.write(f'  "default_core_name": "{ra_configs.default_core_name()}",\n')
        lpl_file.write('  "label_display_mode": 0,\n')
        lpl_file.write('  "right_thumbnail_mode": 3,\n')
        lpl_file.write('  "left_thumbnail_mode": 2,\n')
        lpl_file.write('  "thumbnail_match_mode": 0,\n')
        lpl_file.write('  "sort_mode": 0,\n')
        lpl_file.write('  "items": [\n')
