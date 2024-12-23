# -- coding: UTF-8 --

from common.helper import Helper


class LabelValueZhcn:
    def parse(self, rom_elem):
        return Helper.remove_region(rom_elem.get("zhcn"))
