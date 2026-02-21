# -- coding: UTF-8 --

from helper import Helper
from init_global_configs import Init_Global_Configs
from resource_file_helper import ResourceFileHelper
from roms_db import RomsDB


if __name__ == "__main__":
    Init_Global_Configs()

    for rom in RomsDB.all_roms():
        rom_file_path = ResourceFileHelper.compute_rom_file_path(
            rom, include_crc32=True
        )
        rom_file_exists = rom_file_path.exists()

        if not rom_file_exists:
            rom_file_path = ResourceFileHelper.compute_rom_file_path(
                rom, include_crc32=False
            )
            rom_file_exists = rom_file_path.exists()

        if rom_file_exists:
            rom_crc32 = Helper.compute_crc32(rom_file_path)
            if rom_crc32 != rom.crc32:
                print(
                    f"【错误】{rom.file_name} 的 CRC32 校验失败，实际值={rom_crc32}，预期值={rom.crc32}"
                )
        else:
            print(f"【错误】缺失 ROM 文件 {rom_file_path}")
