# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs

from common.label_value_en import LabelValueEn
from common.label_value_zhcn import LabelValueZhcn

from common.rom_path_value_android import AndroidRomPathValue
from common.rom_path_value_win import WinRomPathValue
from common.rom_path_value_xbox import XBoxRomPathValue

from ra_export_all import RA_ExportAll
from ra_export_fbneo_roms import RA_ExportFBNeoRoms


class RA_ExportFBNeoMenu:
    @staticmethod
    def add_cmds(main_menu):
        ra_export_roms = RA_ExportFBNeoRoms()
        playlist_name_en = "R-Sam - CPS3 Arcade Games (FBNeo)"
        playlist_name_zhcn = "认真玩 - CPS3 街机游戏 (FBNeo)"

        # export to Android in English
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_en
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueEn()
        ra_export_all.rom_path_value = AndroidRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Android (英文)", ra_export_all)

        # export to Android in Simplified Chinese
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_zhcn
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueZhcn()
        ra_export_all.rom_path_value = AndroidRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Android (简中)", ra_export_all)

        # export to Windows in English
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_en
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueEn()
        ra_export_all.rom_path_value = WinRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Windows (英文)", ra_export_all)

        # export to Windows in Simplified Chinese
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_zhcn
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueZhcn()
        ra_export_all.rom_path_value = WinRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Windows (简中)", ra_export_all)

        # export to XBOX in English
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_en
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueEn()
        ra_export_all.rom_path_value = XBoxRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 XBOX (英文)", ra_export_all)

        # export to XBOX in Simplified Chinese
        ra_export_all = RA_ExportAll()
        ra_export_all.playlist_name = playlist_name_zhcn
        ra_export_all.export_roms = ra_export_roms
        ra_export_all.label_value = LabelValueZhcn()
        ra_export_all.rom_path_value = XBoxRomPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 XBOX (简中)", ra_export_all)
