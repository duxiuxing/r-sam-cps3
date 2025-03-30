# -- coding: UTF-8 --

from menu_export_ra_files import Menu_ExportRaFiles
from menu_export_fbneo_files import Menu_ExportFBNeoFiles
from menu_main import MainMenu

from quit import Quit
from r_sam_roms_check import RSamRoms_CheckCrc32, RSamRoms_CheckTitles


if __name__ == "__main__":
    main_menu = MainMenu.instance()

    Menu_ExportRaFiles.add_cmds(main_menu)

    Menu_ExportFBNeoFiles.add_cmds(main_menu)

    # Wii_ExportAll.add_cmds(main_menu)

    RSamRoms_CheckCrc32.add_cmds(main_menu)
    RSamRoms_CheckTitles.add_cmds(main_menu)

    Quit.add_cmds(main_menu)

    main_menu.show()
