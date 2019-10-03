import vk_api



vk = vk_api.VkApi(login="89210078493",password="124536DZ")
vk.auth()
api = vk.get_api()

def getHistory(data):
    user_id = data
    chat = user_id
    history = api.messages.getHistory(offset=0, count=50,  peer_id=chat)
    old = []
    for i in range(len(history['items'])):
        if history['items'][i]['body'].startswith('/инфо'):
            his = history['items'][i]['body'].split('/инфо')
            q = history['items'][i]['chat_id']
            x = history['items'][i]['from_id']
            for i in range(len(his)):
                if his[i].startswith('#'):
                   z = his[i].split('#')
                   old.append(z[1:])


    return old,q,x

def getHistory1(data):
    user_id = data
    chat = user_id
    history = api.messages.getHistory(offset=0, count=20,  peer_id=chat)
    old = []
    for i in range(len(history['items'])):
        if history['items'][i]['body'].startswith('/инфо'):
            his = history['items'][i]['body'].split('/инфо')
            q = history['items'][i]['chat_id']
            x = history['items'][i]['from_id']
            for i in range(len(his)):
                if his[i].startswith('#'):
                   z = his[i].split('#')
                   old.append(z[1:])


    return history

def get_user(data):
    user_id = data
    screen = api.users.get(user_ids=user_id,fields = 'screen_name',name_case="Nom")
    return screen

#def get_conf(data):

def sendDocs():
    down = api.docs.getMessagesUploadServer(type='doc',peer_id = 29353463)
    return down



if __name__ == '__main__':
        #oldlist,chatold,userold =getHistory(2000000004)
        #print(oldlist)
        #print(getHistory1(2000000004))
        print(sendDocs())

        #print(get_user(285515351))

