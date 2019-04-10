# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.
users=db.users

fishes={}
world={
    'grassland':{
        'blocks': 100,    # Количество блоков на данном участке. Участки всегда квадратные. 100 блоков значит, что участок 10х10 блоков.
        'depth': 10,      # Глубина.  1й блок - граница с воздухом, последний - дно.
        'nearlocs':{      # Ближайшие локации. Т.к. участко это куб, локации могут быть справа, слева, спереди и сзади относительно текущего.
            'right':None,
            'left':None,
            'up':None,
            'down':'rockland'
            
        }
        
    },
    
    'rockland':{
        'blocks': 100,    
        'depth': 18,      
        'nearlocs':{      
            'right':None,
            'left':None,
            'up':'grassland',
            'down':None
            
        }
    }

}


# Один блок представляет из себя пространство 3х3 метров.


try:
    pass

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(441399484, traceback.format_exc())

    
    
    
    
    
def life():
    checktime=1
    for ids in fishes:
        fishes[ids].action()
    t=threading.Timer(checktime, life)
    t.start()
    
    
    
print('7777')
bot.polling(none_stop=True,timeout=600)

