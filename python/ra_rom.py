# -- coding: UTF-8 --


class RA_Rom:
    def __init__(
        self,
        file_path,
        label,
        crc32,
        playlist_name,
    ):
        self.file_path = file_path
        self.label = label
        self.crc32 = crc32
        self.playlist_name = playlist_name
