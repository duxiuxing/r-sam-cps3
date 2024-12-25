# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from common.label_value import EnLabelValue, ZhcnLabelValue
from common.path_value import AndroidPathValue, WinPathValue, XBoxPathValue

from ra_export_all import RA_ExportAll
from ra_export_fbneo_roms import RA_ExportFBNeoRoms


class RA_ExportFBNeoMenu:
    @staticmethod
    def add_cmds(main_menu):
        export_roms = RA_ExportFBNeoRoms()
        playlist_name_en = "R-Sam - CPS3 Arcade (FBNeo)"
        playlist_name_zhcn = "认真玩 - CPS3 街机 (FBNeo)"

        # export to Android in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = AndroidPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Android (英文)", export_all)

        # export to Android in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = AndroidPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Android (简中)", export_all)

        # export to Windows in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = WinPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 Windows (英文)", export_all)

        # export to Windows in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = WinPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 Windows (简中)", export_all)

        # export to XBOX in English
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_en
        export_all.playlist_label_value = EnLabelValue()
        export_all.playlist_path_value = XBoxPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_en} 到 XBOX (英文)", export_all)

        # export to XBOX in Simplified Chinese
        export_all = RA_ExportAll()
        export_all.export_roms = export_roms
        export_all.playlist_name = playlist_name_zhcn
        export_all.playlist_label_value = ZhcnLabelValue()
        export_all.playlist_path_value = XBoxPathValue()
        main_menu.add_cmd(f"导出 {playlist_name_zhcn} 到 XBOX (简中)", export_all)
