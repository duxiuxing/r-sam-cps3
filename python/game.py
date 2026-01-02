# -- coding: UTF-8 --


class Game:
    def __init__(self, id, en_title):
        self.id = id
        self.en_title = en_title
        self.zhcn_title = ""
        self.rom_list = []
        self.developer = ""
        self.publisher = ""
        self.genre = ""
        self.date = ""
        self.players = ""
