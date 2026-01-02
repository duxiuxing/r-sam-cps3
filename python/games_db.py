# -- coding: UTF-8 --

from game import Game


class GamesDB:
    __instance = None

    @staticmethod
    def instance():
        if GamesDB.__instance is None:
            GamesDB()
        return GamesDB.__instance

    def __init__(self):
        GamesDB.__instance = self
        self.__id_to_game = {}
        self.__name_to_game = {}

    def add_game(self, game: Game):
        self.__id_to_game[game.id] = game

    def query_game_by_id(self, game_id):
        return self.__id_to_game.get(game_id)
