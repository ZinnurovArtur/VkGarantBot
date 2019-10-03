# -*- coding: utf-8 -*-
import commands1


def hello():
    attachment = 'photo491182752_456239041'
    message=    "Привет. Я Гарант-Бот!\nВведите /инфо чтоб ввести данные.\nЕсли данные неправильны-введите /стоп и напишите /инфо снова.\nДАННЫЕ ВВОДИТ ТОЛЬКО ПОКУПАТЕЛЬ\n\nПравила и инструкции: https://vk.com/wall498986116_4\nНапиши '/помощь', чтобы получить список команд."
    return message,attachment


hello_command = commands1.Command()

hello_command.keys = ['/старт']
hello_command.description = 'Запуск бота '
hello_command.process = hello