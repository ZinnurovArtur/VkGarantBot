# -*- coding: utf-8 -*-
commandlist = []

class Command:
    def __init__(self):
        self.__keys =[]
        self.description =''
        commandlist.append(self)

    def keys(self):
        return self.__keys()

    def keys(self,mas):
        for k in mas:
            self.__keys.append(k.lower())
    def process(self):
        pass