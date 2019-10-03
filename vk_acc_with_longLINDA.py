# -*- coding: utf-8 -*-
import vk_api
from replyes import createanswer,IFgroup,adushevPrivate
from datetime import datetime
import traceback
import requests
import time
from data import read,surname,total
import shutil
import pandas as pd
import string
import random


def DF_Time():
    time = str(datetime.now())
    time = time.split( )
    time = time[1]
    time = time[0:len(time) - 7]
    return time

#Нужные переменные советую держать в отдельном config-файле, здесь просто для удобства воткнул.




#code = two_factor()

#Объявим переменную вк в самом коде, чтобы обращаться к ней, не передавая в функции. Ваш кэп.
vk = vk_api.VkApi(login="login",password="pass")
vk.auth()
api = vk.get_api()


def users(data):
    user_id = data
    everyone = api.users.get(user_ids=user_id,fields = 'screen_name',name_case='Nom')
    return everyone




def getHistoryuser(data,user):
    history=api.messages.getHistory(offset=0,count=15,peer_id =data)
    info =[]
    userid=0
    for i in range(len(history['items'])):
        if history['items'][i]['from_id']==498986116:
                temp = history['items'][i]['body'].split('\n')
                for i in range(len(temp[1:7])):
                    history1 = temp[1:][i].split(': ')
                    print(history1)
                    info.append(history1[1])
        if history['items'][i]['from_id']==user and history['items'][i]['body'].isdigit():
            userid = history['items'][i]['from_id']

    return info,userid





def getHistoryinfo(data,fromid):
    history=api.messages.getHistory(offset=0,count=10,peer_id =data)
    allid =[]


    for i in range(len(history['items'])):
            if history['items'][i]['from_id'] == fromid and len(allid)!=5 :
                allid.append(history['items'][i]['body'])
    return allid

def gethistorymess(data):
    history=api.messages.getHistory(offset=0,count=2,peer_id =data)
    allold=[]
    for i in range(len(history['items'])):
            allold.append(history['items'][i]['body'])
    return allold


def IFgroup(data,messages,attachment=""):
    user_id = data
    if user_id - 2000000000 > 0:
        chat_id = data-2000000000
        api.messages.send(chat_id=chat_id,message=messages,attachment=attachment)
    else:
        api.messages.send(user_id=user_id,message=messages,attachment=attachment)

def randomsPASS():
    char = string.ascii_uppercase+\
           string.ascii_lowercase+\
           string.digits
    size = random.randint(8,16)
    return ''.join(random.choice(char)for i in range(size))

def sendDocs():
   save= api.docs.getMessagesUploadServer(type='doc',peer_id=71561155)
   path = "/home/arthur5233/test1.csv"
   r= requests.post(save['upload_url'],files ={'file':open(path,"rb")})
   params = {'file': r.json()['file']}
   doc = api.docs.save(file = params['file'],title='zakazi')
   finddoc = api.docs.get(count = 1,offset =0,type =0)
   return finddoc


def mult(test,user):
    precent = (test*3)/100
    if precent <200:
        IFgroup(user,"Минимальная оплата услуг 200 руб")
        price = 200 + test
        return price
    else:
        price = precent+test
        return price

def addUser():
    getlist = api.friends.getRequests(offset = 0,count = 100,need_viewed=1,follow=1)
    if getlist['count']>0:
        for i in range(len(getlist['items'])):
            try:
                api.friends.add(user_id=getlist['items'][i], text='cool')
            except vk_api.exceptions.ApiError:
                api.friends.delete(user_id=getlist['items'][i])
    else:
        return 0







def acc_work():
    #Получаем лонг собсна. Советую время от времени проверять актуальную IP-версию. На сегодняшний день – 3.
    long = vk.method('messages.getLongPollServer', {'need_pts':1, 'Ip_version':3})
    while 1:
        #проверка на входящие сообщения. Порой случаются моменты, когда некоторые сообщения лонг не ловит, чаще из-за сбоев или отключения.
        #old_messages = check_mess()
        adding =addUser()
        response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=90&mode=2&version=3'.format(server=long['server'], key=long['key'], ts=long['ts'])).json()
        if 'updates' in response:
            #messages = old_messages #Далее формируем список, в который будет входить информация о запросах.
            for z in range(len(response['updates'])):
                if response['updates'][z][0] == 4:
                    try:
                        res1=getHistoryinfo(int(response['updates'][z][3]), int(response['updates'][z][6]['from']))
                    except:
                        KeyError

                    summands = []
                    flag = response['updates'][z][2]

                    #этот интересный фрагмент кода я нашел в интернете. Думаю, побитовое И тебе известно, разберешься, в чем тут соль.
                    #p.s. это делается для того, чтобы избежать ответов на собственные сообщения бота - они тоже почему-то попадают в response ._.
                    #подробнее можно здесь почитать: vk.com/dev/using_longpoll_2?f=4.%2BФлаги%2Bсообщений

                    for number in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 65536]:  # проходим циклом по возможным слагаемым
                        if flag & number:  # проверяем, является ли число слагаемым с помощью побитового И
                            summands.append(number)  # если является, добавляем его в массив
                    if 2 not in summands: #если это не исходящее от бота сообщение:
                        #здесь сам посмотришь, что передается в доп. полях и какую инфу ты хочешь сохранять. Мне достаточно айди и сообщения.
                        user_id = response['updates'][z][3]
                        message = response['updates'][z][5]
                        keys = ['/Yes','/yes','/да','\yes','\Yes']

                        try:
                            groupuser = response['updates'][z][6]['from']
                        except:
                            KeyError

                        user_flag = False




                        print(response)

                        if message == '/инфо':
                            IFgroup(user_id,"Введите откуда товар(без запятых и других символов)")



                        elif "Введите откуда товар(без запятых и других символов)" in gethistorymess(user_id) and message!='/стоп':
                            IFgroup(user_id,'Введите куда вы хотите отправить товар')


                        elif "Введите куда вы хотите отправить товар" in gethistorymess(user_id) and message!='/стоп':
                            IFgroup(user_id,'Введите состояние товара')



                        elif 'Введите состояние товара' in gethistorymess(user_id) and message!='/стоп':
                            IFgroup(user_id, "Введите цену только ЦИФРАМИ")


                        elif "Введите цену только ЦИФРАМИ" in gethistorymess(user_id) and message!='/стоп':
                            if message.isdigit()== False:
                                IFgroup(user_id,"Введите цену цифрами\nПовторите через /инфо")
                            else:
                                IFgroup(user_id,"Карта продавца без пробелов")
                                IFgroup(user_id,'Обращаем ваше внимание что вы должны попросить карту ЗАРАНЕЕ у продавца')

                        elif "Обращаем ваше внимание что вы должны попросить карту ЗАРАНЕЕ у продавца" in gethistorymess(user_id) and message!='/стоп':
                            if len(message) != 16:
                                IFgroup(user_id,"Введите все 16 чисел карты\nПовторите через команду  /инфо")


                            else:
                                z = res1[::-1]





                                IFgroup(user_id,
                                        "Правильные данные?" + '\n' + "Откуда: " + str(z[0]) + '\n' + "Куда: " + str(
                                            z[1]) + '\n' +
                                        "Состояние: " + str(z[2]) + '\n' + "Цена: " + str(z[3]) + '\n' +
                                        "Карта продавца: " +str(z[4]) +'\n'+
                                        "Ссылка покупателя: https://vk.com/id" + groupuser + '\n' +
                                        "Чтобы потвердить сделку, введите  одно из " + str(keys) + '\n' +
                                        "Если информация введена неверно,повторите ввод через команду /инфо")

                        elif message == '/стоп':
                            IFgroup(user_id,"Выход из заполнения")












                        elif (message in keys):
                            list1,olduser2 = getHistoryuser(user_id, int(groupuser))
                            if int(response['updates'][z][6]['from']) == olduser2:
                                z =list1[:-1]

                                z.append(random.randint(1, 1000000))
                                z.append(randomsPASS()[:4])
                                try:
                                    z.append(int(total())+int(z[3]))
                                except:
                                    FileNotFoundError

                                file = ["Откуда,Куда,Состояние,Цена,Карта продавца,ID,PASS,TOTAL".split(","),
                                        z]
                                my_list = []
                                fieldnames = file[0]
                                print(file[1:])
                                for values in file[1:]:
                                    inner_dict = dict(zip(fieldnames, values))
                                    my_list.append(inner_dict)
                                # print(write(my_list, fieldnames),"price")
                                print(surname(my_list, fieldnames))
                                shutil.copy("test1.csv", "copyTest1.csv")
                                print(my_list)

                                price1 = mult(int(z[3]),user_id)
                                IFgroup(user_id, "Итого " + str(price1) + "руб" +
                                        "\n" + "Ваш ID" + str(z[5]) + "\n" +
                                        "Ждем оплаты: " +
                                        '\n' + '4274270013499256')
                                adushevPrivate(71561155, "Заказ цена которого" + '\n' + str(int(price1))+'руб' + '\n' +
                                               'ID' + str(z[5]) + '\n' + 'Карта продавца: '+str(z[4])+'\n'+'Цена: '+str(price1)+
                                               '\n'+
                                               'Ссылка покупателя: https://vk.com/id'+str(olduser2)+'\n'
                                               +'Чтоб потвердить,напишите ' + '\n' + '/go' + str(
                                    int(z[5])),"")


                                adushevPrivate(olduser2, 'Ваш ID ' + str(z[5]) + '\n' + 'Ваш пароль: ' + str(z[6]) +
                                               '\n' +
                                               'После получения товара введите "/товар пароль" в беседе, если товар соответсвует описанию.\nЕсли нет, введите /помощь в беседе',
                                               'photo491182752_456239026')
                            else:
                                IFgroup(user_id,"Доступ только покупателям")








                        elif message.startswith('/go') and user_id == 71561155:
                            cena = message[3:]
                            cena1 ="ID"+cena
                            search = api.messages.search(q=cena1, count=4, offset=0)


                            for i in range(len(search['items'])):
                                try:
                                    if search['items'][i]['chat_id']:
                                        peer1 = int(search['items'][i]['chat_id'])+2000000000

                                        IFgroup(peer1, "Деньги получены  "+cena1+'\n'+"Товар может быть отправлен.\nПосле получения товара покупатель должен ввести /товар пароль, если с товаром все хорошо."
                                        "\nВ противном случае введите /проблемы")

                                    else:
                                        print("NO")
                                except:
                                    KeyError

                        elif message.startswith('/товар '):
                            tovar = message[7:]
                            a =read()
                            for i in range(len(a)):
                                print(a[i]['Pass'])
                                if tovar==a[i]['Pass']:
                                    IFgroup(user_id,"Товар получен!\nДеньги в скором времени будут отправлены на карту продавца\nОставьте отзыв https://vk.com/wall498986116_5. Это очень важно для нашего проекта!")
                                    adushevPrivate(71561155,
                                                "Товар получен у заказа " + str(a[i]['id']) + '\n' + "Карта продавца: " +
                                                   str(a[i]['card'])+'\n'+"Цена: "+str(a[i]['price']))

                                    df = pd.read_csv('/home/arthur5233/test1.csv', encoding='utf-8')
                                    for index, row in df.iterrows():
                                        if row['PASS'] == a[i]['Pass']:
                                            df.drop(index,inplace=True)
                                            df.to_csv('/home/arthur5233/test1.csv',index_label='Откуда',index=False)

                                    break

                            else:
                                IFgroup(user_id, "Неправильный пароль или данные")

                        elif message == '/проблемы':
                            chat = user_id-2000000000
                            getVanya = api.messages.addChatUser(chat_id = chat,user_id=71561155)

                        elif message in ['/doc','/документы','/Документы'] and user_id in [71561155,29353463]:
                            file = sendDocs()

                            idfile ='doc{owner}_{id}'.format(owner=498986116,id=file['items'][0]['id'])
                            if user_id == 29353463:
                                adushevPrivate(29353463,"Документ",idfile)
                            else:
                                adushevPrivate(71561155,"Документ",idfile)




                        else:
                            try:
                                createanswer(message,user_id)
                            except:
                                vk_api.ApiError




            try:
                long['ts'] = response['ts']
            except:
                long = vk.method('messages.getLongPollServer', {'need_pts':1, 'Ip_version':3})

#считай, страховочная оболочка для работы бота, чтобы он пытался перезапуститься самостоятельно. Порой бывают исключения в сообщениях, их можно решать
#отправкой отчета об ошибке + прочтением этого сообщения с помощью метода api и дальнейшей работы. Ну ты поймешь.




while 1:
    try:
        acc_work()

    except:
        print(traceback.format_exc()) #здесь сам пропиши нужные тебе исключения в случае проблемы с работой аккаунта. traceback я тебе импортировал.
        with open("/home/arthur5233/log.txt", 'a+',encoding='utf-8') as file:
            file.write('\n'+time.asctime()+'\n\n'+traceback.format_exc())
            file.close()

        time.sleep(0.5)

