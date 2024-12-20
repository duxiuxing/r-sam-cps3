# -- coding: UTF-8 --

from cmd_handler import CmdHandler


class CmdQuit(CmdHandler):
    def __init__(self):
        super().__init__("退出程序")

    def run(self):
        exit()
