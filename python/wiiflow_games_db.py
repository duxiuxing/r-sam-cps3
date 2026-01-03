# -- coding: UTF-8 --

from wiiflow_game import WiiFlow_Game


class WiiFlow_GamesDB:
    __instance = None

    @staticmethod
    def instance():
        if WiiFlow_GamesDB.__instance is None:
            WiiFlow_GamesDB()
        return WiiFlow_GamesDB.__instance

    def __init__(self):
        WiiFlow_GamesDB.__instance = self
        self.__id_to_game = {}

    def all_game_ids(self):
        return self.__id_to_game.keys()

    def all_games(self):
        return self.__id_to_game.values()

    def add_game(self, game: WiiFlow_Game):
        self.__id_to_game[game.id] = game

    def query_game(self, game_id=None, game_title=None):
        if game_id is not None:
            game = self.__id_to_game.get(game_id)
            if game is not None:
                return game

        if game_title is not None:
            for game in self.all_games():
                if game_title == game.en_title:
                    return game
                if game_title == game.zhcn_title:
                    return game

        return None
