import imp
from re import search
from urllib import request
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id 
import vk_api
import random

# токен Антона e3ed02627e712e74819d8b3a08141d06612fdc171e7eec53a5687bb1af72f3e882bd38a659e38443fc015
# мой токен 569835b6de78352c52149ae49dabb3981304101e3f1c73f9f99e194c7cd40dbbeebf6e6e4120782a5ff6c

token = 'e3ed02627e712e74819d8b3a08141d06612fdc171e7eec53a5687bb1af72f3e882bd38a659e38443fc015'

vk = vk_api.VkApi(token = token)
longpoll: VkLongPoll = VkLongPoll(vk)
session_api = vk.get_api()

def photo(photo1):
    global attachment
    upload = vk_api.VkUpload(session_api)
    photo = upload.photo_messages(photo1)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

def solveMessage(chat_id, text):
    try:
        solve = str(eval(event.text))
        ans = str('Ответ: ' + solve)
        session_api.messages.send(peer_id = event.peer_id, random_id = 0, message =  ans)
    except:
        session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Увы, но я пока что не знаю как на это ответить')

def yes_no(chat_id, text):
    num = random.randint(1, 2)
    if num == 1:
        session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Да')
    else:
        session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Нет')


#123

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Покажи Илью' or event.text == 'покажи илью' or event.text == 'покажи илью.' or event.text == 'Покажи илью.' :
            photo('panda.png')
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, attachment = attachment)
        elif event.text == 'Биба' or event.text == 'биба':
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Да биба, и что?')
        elif event.text == 'Привет' or event.text == 'привет':
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'О, привет!')
        elif ('!' in event.text):
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Эу, не кричи на меня')
        elif event.text == 'А кто слева?' or event.text == 'а кто слева?' or event.text == 'кто слева?' or event.text == 'слева кто?' or event.text == 'Слева кто?' or event.text == 'Кто слева?':
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Илья')
        elif ('?' in event.text):
            yes_no(event.chat_id, event.text)
        elif event.text == 'Боба' or event.text == 'боба':
            session_api.messages.send(peer_id = event.peer_id, random_id = 0, message = 'Нет биба')

        else:
            solveMessage(event.chat_id, event.text)
       
       
            

        
            

        




        

  
        
      
