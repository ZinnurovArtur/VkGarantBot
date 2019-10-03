# -*- coding: utf-8 -*-
import commands1

def tovar():
    message = 'Когда товар получен и он соответствует описанию, введите /товар пароль'
    attachment = 'photo491182752_456239026'
    return message,attachment

info_command = commands1.Command()

info_command.keys = ["/товар"]
info_command.description = "Товар получен и соотвествует описанию. Пароль отправлен в личку покупателю"
info_command.process = tovar