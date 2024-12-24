# -- coding: UTF-8 --


class CmdQuit:
    @staticmethod
    def add_cmds(main_menu):
        main_menu.add_cmd("退出程序", CmdQuit())

    def run(self):
        exit()
