# -*- coding: utf-8 -*-
import commands1


def problem():
    message = ""
    return message,''

info_command = commands1.Command()

info_command.keys = ['/проблемы','/проблемы']
info_command.description = "Позвать гаранта"
info_command.process = problem