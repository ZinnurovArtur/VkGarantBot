# -*- coding: utf-8 -*-
import commands1

def help():
	message = ''
	attachment = 'photo491182752_456239041'
	for c in commands1.commandlist:
		message += c.keys[0] + ' ---' + c.description + '\n'+'\n'
	return message,attachment

help_command = commands1.Command()

help_command.keys = ['/помощь','хелп','помощь']
help_command.description = "Покажу список команд"
help_command.process = help