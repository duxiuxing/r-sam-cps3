# -- coding: UTF-8 --

from common.console_configs import ConsoleConfigs
from export_roms_base import ExportRomsBase
from ra_export_playlist import RA_ExportPlaylist
from ra_export_thumbnails import RA_ExportThumbnails


class RA_ExportFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=False,
        )


class RA_ExportFakeFBNeoRoms(ExportRomsBase):
    def __init__(self):
        super().__init__(
            xml_file_name="fbneo-roms-export.xml",
            dst_roms_folder_name=f"Arcade (FinalBurn Neo)\\{ConsoleConfigs.short_name()}",
            export_fake_roms=True,
        )


if __name__ == "__main__":
    export_roms = RA_ExportFBNeoRoms()
    export_roms.run()

    lpl_file_name = f"认真玩 - {ConsoleConfigs.zhcn_name()}游戏 (FBNeo)"
    label_in_xml = "zhcn"

    RA_ExportPlaylist(
        lpl_file_name=lpl_file_name,
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml=label_in_xml,
    ).run()

    RA_ExportThumbnails(
        lpl_file_name=lpl_file_name,
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml=label_in_xml,
    ).run()

    """
    lpl_file_name = f"R-Sam - {ConsoleConfigs.en_name()} Games (FBNeo)"
    label_in_xml = "en"

    RA_ExportPlaylist(
        lpl_file_name=lpl_file_name,
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml=label_in_xml,
     ).run()

    RA_ExportThumbnails(
        lpl_file_name=lpl_file_name,
        rom_crc32_to_dst_rom_path=export_roms.rom_crc32_to_dst_rom_path,
        xml_file_name=export_roms.xml_file_name,
        label_in_xml=label_in_xml,
    ).run()
    """
