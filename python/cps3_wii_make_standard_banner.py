# -- coding: UTF-8 --

from wii_make_standard_banner import S_BannerInfo, Wii_MakeStandardBanner


if __name__ == "__main__":
    sfiii_banner_info = S_BannerInfo(
        "sfiii",
        game_logo_size=(240, 120),
        game_logo_left_top=(-24, 18),  # 左上
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_BOTTOM,
    )

    sfiii2_banner_info = S_BannerInfo(
        "sfiii2",
        game_logo_size=(240, 120),
        game_logo_left_top=(6, 208),  # 左下
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    sfiii3_banner_info = S_BannerInfo(
        "sfiii3",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    jojo_banner_info = S_BannerInfo(
        "jojo",
        game_logo_size=(160, 80),
        game_logo_left_top=(418, 250),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    jojoba_banner_info = S_BannerInfo(
        "jojoba",
        game_logo_size=(270, 150),
        game_logo_left_top=(306, 122),  # 右中
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )

    sfiii2_banner_info = S_BannerInfo(
        "sfiii2",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        capcom_logo_left_top=S_BannerInfo.CAPCOM_LOGO_ALIGN_RIGHT_TOP,
    )
    
    Wii_MakeStandardBanner(sfiii2_banner_info).run()
