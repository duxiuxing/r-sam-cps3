# -- coding: UTF-8 --

from wii_make_widescreen_banner import W_BannerInfo, Wii_MakeWidescreenBanner


if __name__ == "__main__":
    sfiii_banner_info = W_BannerInfo(
        "sfiii",
        game_logo_size=(540, 270),
        game_logo_left_top=(156, 40),  # 水平居中，垂直靠下
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
        capcom_logo_left_top=W_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
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
        capcom_logo_left_top=W_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    Wii_MakeWidescreenBanner(sfiii_banner_info).run()
