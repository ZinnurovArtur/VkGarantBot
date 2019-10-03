# -*- coding: utf-8 -*-
import commands1

def info():
    message = ''
    attachment = 'photo491182752_456239041'
    return message,attachment

info_command = commands1.Command()

info_command.keys = ['/инфо ']
info_command.description = "Ввод данных о сделки.\nДанные вводит ТОЛЬКО ПОКУПАТЕЛЬ.\nЕсли данные неправильны или вы ошиблись -" \
                           "\nНапишите /стоп потом повторите командой /инфо.  "
info_command.process = info