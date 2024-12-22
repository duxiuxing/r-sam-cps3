# -- coding: UTF-8 --


class CmdHandler:
    def __init__(self, tips):
        self.tips = tips

    def run(self):
        raise NotImplementedError()
