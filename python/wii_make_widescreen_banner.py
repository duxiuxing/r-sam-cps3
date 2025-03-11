# -- coding: UTF-8 --

import os

from console_configs import ConsoleConfigs
from game_info import GameInfo
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from wiiflow_plugins_data import WiiFlowPluginsData


class W_BannerInfo:
    CAPCOM_LOGO_WIDTH = 142
    CAPCOM_LOGO_HEIGHT = 29
    CAPCOM_LOGO_OFFSET_X_TOP = 39
    CAPCOM_LOGO_OFFSET_Y = 8
    CAPCOM_LOGO_ALIGN_LEFT_TOP = (39, 8)
    CAPCOM_LOGO_ALIGN_TOP_RIGHT = (649, 8) # 649=830-142-39

    MENU_SCREEN_WIDTH = 830
    MENU_SCREEN_HEIGHT = 332

    def __init__(
        self, rom_title, game_logo_size, game_logo_left_top, capcom_logo_left_top
    ):
        self.rom_title = rom_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.capcom_logo_left_top = capcom_logo_left_top


class Wii_MakeWidescreenBanner:
    def __init__(self, banner_info):
        self.banner_info = banner_info
        self.game_info = WiiFlowPluginsData.instance().query_game_info(
            rom_title=banner_info.rom_title
        )

    def make_main_screen_bg(self):
        main_screen_bg_path = os.path.join(
            LocalConfigs.repository_directory(),
            f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen-bg.png",
        )
        if os.path.exists(main_screen_bg_path):
            return Image.open(main_screen_bg_path)
        else:
            wallpaper_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\wallpaper\\{self.game_info.name}.jpg",
            )
            image = Image.open(wallpaper_path).resize(
                (W_BannerInfo.MENU_SCREEN_WIDTH, W_BannerInfo.MENU_SCREEN_HEIGHT)
            )
            Helper.verify_exist_directory_ex(os.path.dirname(main_screen_bg_path))
            image.save(main_screen_bg_path, format="PNG")
            return image

    def run(self):
        main_screen_bg = self.make_main_screen_bg()
        main_screen_bg_changed = False

        if self.banner_info.game_logo_size != (0, 0):
            game_logo_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"image\\logo\\{self.game_info.name}.png",
            )
            game_logo = Image.open(game_logo_path).resize(
                self.banner_info.game_logo_size
            )
            main_screen_bg.paste(
                game_logo, self.banner_info.game_logo_left_top, mask=game_logo
            )
            main_screen_bg_changed = True

        if self.banner_info.capcom_logo_left_top != (0, 0):
            capcom_logo_path = os.path.join(
                LocalConfigs.repository_directory(), "image\\logo\\capcom.png"
            )
            capcom_logo = Image.open(capcom_logo_path).resize(
                (W_BannerInfo.CAPCOM_LOGO_WIDTH, W_BannerInfo.CAPCOM_LOGO_HEIGHT)
            )
            main_screen_bg.paste(
                capcom_logo, self.banner_info.capcom_logo_left_top, mask=capcom_logo
            )
            main_screen_bg_changed = True

        if main_screen_bg_changed:
            main_screen_path = os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen.png",
            )
            main_screen_bg.save(main_screen_path)

        main_screen_bg.resize((590, 332)).save(
            os.path.join(
                LocalConfigs.repository_directory(),
                f"wii\\wad\\{self.game_info.rom_title}\\res\\widescreen\\MenuScreen1.png",
            ),
        )


if __name__ == "__main__":
    sfiii_banner_info = W_BannerInfo(
        "sfiii",
        game_logo_size=(540, 270),
        game_logo_left_top=(156, 40), # 水平居中，垂直靠下
        capcom_logo_left_top=W_BannerInfo.CAPCOM_LOGO_ALIGN_LEFT_TOP,
    )

    sfiii2_banner_info = W_BannerInfo(
        "sfiii2",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=(0, 0),
    )

    sfiii3_banner_info = W_BannerInfo(
        "sfiii3",
        game_logo_size=(400, 200),
        game_logo_left_top=(430, 85),  # 水平靠右，垂直居中
        capcom_logo_left_top=W_BannerInfo.CAPCOM_LOGO_ALIGN_TOP_RIGHT,
    )

    jojo_banner_info = W_BannerInfo(
        "jojo",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=(0, 0),
    )

    jojoba_banner_info = W_BannerInfo(
        "jojoba",
        game_logo_size=(270, 150),
        game_logo_left_top=(273, 182),  # 水平居中，垂直靠下
        capcom_logo_left_top=W_BannerInfo.CAPCOM_LOGO_ALIGN_TOP_RIGHT,
    )

    Wii_MakeWidescreenBanner(sfiii_banner_info).run()
