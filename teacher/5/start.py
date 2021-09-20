from gamelib import make_deck # функция по созданию колоды
import telebot
key = '1765842295:AAH_Vj8ti5WSjsU5mUFS7U3tOY2AmCinkAY'
bot = telebot.TeleBot(key)
import random

import os.path
import json
from db import read_db, write_db, add_user

# s = json.loads('[1,2,3]') json.dumps([1,2,3])



# user = [
#     {"username": 'ddd', "ctat_id": }
# ]

@bot.message_handler()
def just_a_message(message):
    print(message.json['text'])



@bot.message_handler(commands=['start'])
def start_message(message):
    deck = make_deck()
    rc = random.randint(0,len(deck)-1)
    bot.send_message(message.chat.id, deck[rc]["name"])
    rezult = add_user(message.from_user.username, message.chat.id)

    db = read_db()
    for user in db:
        if rezult:
            mes = 'У нас новый чел %s' % message.from_user.username
            bot.send_message(user["chat_id"], mes)

    # записываю в бд
    # users = read_db()
    # users.append({"username": message.from_user.username, "chat_id": message.chat.id})
    # write_db(users)

    #bot.send_photo(chat_id=message.chat.id, #photo=open(f'cards/{deck[rc]["name"]}', 'rb'))
    #photo=open('cards/1.jpeg','rb'))


    #bot.send_message(message.chat.id, 'Привет %s, ты написал мне /start' % message.from_user.username)

# deck = make_deck()
# print(deck)
print('Starting bot.....')
bot.polling()