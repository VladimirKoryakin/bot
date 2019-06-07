import random
import vk_api
import requests 
from vk_api.longpoll import VkLongPoll, VkEventType 
vk_session = vk_api.VkApi(token='ffee8fff00f944d706dd455eeb8eedf8269d7403122bcee3fabe31bea8d6d147a3e7be2f253ef6d2b8a96')
vk = vk_session.get_api() 
for event in VkLongPoll(vk_session).listen(): 
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: 
        if event.from_user: #Если написали в ЛС 
            s = event.text 
            if s[:8] == 'Зашифруй': 
                n = s[9]
                i=10
                while True:
                    try:
                        e=int(s[i])
                        n+=s[i]
                    except:
                        break
                    i+=1
                n=int(n)
                c = s[i+1:] 
                i0 = n%len(c) 
                new_c = c[len(c) - i0:] + c[:len(c) - i0] 
                vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message=new_c 
                    )
            elif s[:9] == 'Расшифруй':
                n = s[9]
                i=10
                while True:
                    try:
                        e=int(s[i])
                        n+=s[i]
                    except:
                        break
                    i+=1
                n=int(n)
                c = s[i+1:] 
                i0 = len(c)-n%len(c) 
                new_c = c[len(c) - i0:] + c[:len(c) - i0] 
                vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message=new_c 
                )
            else:
                vk.messages.send(user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message='Напиши мне:'+'\n'+'-Зашифруй [число] [слово] (бот выдаст тебе это же слово, но зашифрованное шифром Цезаря)'+'\n'+'-Расшифруй [число] [слово, зашифрованное шифром Цезаря] (бот выдаст тебе тоже слово, но расшифрованное)'+'\n'+'Шифр Цезаря - это обычное шифрование сдвигом'+'\n'+'Например, если ты напишешь: Зашифруй 1 мама'+'\n'+'Бот ответит: амам')
