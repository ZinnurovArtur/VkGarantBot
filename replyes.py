# -*- coding: utf-8 -*-
import vk_api
import os
import importlib
from commands1 import commandlist

vk = vk_api.VkApi(login="89210078493",password="124536DZ")
vk.auth()

api1 = vk.get_api()


def send_messages(user_id, message, attachment=""):

    api1.messages.send(user_id=str(user_id), message=message, attachment=attachment)


def load():
    files = os.listdir("/home/arthur5233/mysite/alpha/commands")
    modules = filter(lambda x: x.endswith('py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def getanswer(body):
    message = ""
    attachment = ''
    for c in commandlist:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment







def createanswer(data,id):
    load()
    user_id = id
    if user_id - 2000000000 > 0:
        chat_id = user_id-2000000000

        message, attachment = getanswer(data.lower())
        api1.messages.send(chat_id = chat_id,message=message,attachment=attachment)
    else:
        message, attachment = getanswer(data.lower())
        send_messages(user_id, message, attachment)

def IFgroup(data,messages):
    user_id = data[3]
    if user_id - 2000000000 > 0:
        user_id1 = data[6]['from']
        chat_id = data[3]-2000000000
        api1.messages.send(chat_id=chat_id,message=messages)
    else:
        api1.messages.send(user_id=user_id,message=messages)

def adushevPrivate(data,messages,attachment=""):
    user_id =data
    api1.messages.send(user_id=user_id,message=messages,attachment=attachment)

def historyMessage(data,responses2):
    user_id = data[3]
    if user_id - 2000000000 > 0:
        user_id1 = data[6]['from']
        chat_id = data[3]-2000000000
        chat = chat_id + 2000000000
        api1.messages.send(chat_id = chat_id ,message = "Откуда: " + str(responses2[-1]) + "\n" + "Куда: " + str(responses2[-2]) + '\n' +
                                    "Состояние: " +
                                   str(responses2[-3]) + '\n' +
                                   "Цена: " + str(responses2[-4])+"\n"+"Карта продавца: "+ str(responses2[-5]))
    else:
        api1.messages.send(user_id=user_id, message="Откуда: "+str(responses2[-1])+"\n"
        +"Куда:" +str(responses2[-2])+'\n'+
        "Состояние: " + str(responses2[-3]) + '\n' +
        "Цена: " + str(responses2[-4]))

