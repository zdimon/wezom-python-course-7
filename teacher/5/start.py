from gamelib import make_deck # функция по созданию колоды
import telebot
key = '1765842295:AAH_Vj8ti5WSjsU5mUFS7U3tOY2AmCinkAY'
bot = telebot.TeleBot(key)
import random

import os.path

if not os.path.isfile('users.json'):
    with open('users.json', 'w') as f:
        f.write('[]')

# user = [
#     {"username": 'ddd', "ctat_id": }
# ]

@bot.message_handler(commands=['start'])
def start_message(message):
    deck = make_deck()
    rc = random.randint(0,len(deck)-1)
    bot.send_message(message.chat.id, deck[rc]["name"])

    bot.send_photo(chat_id=message.chat.id, #photo=open(f'cards/{deck[rc]["name"]}', 'rb'))
    photo=open('cards/1.jpeg','rb'))


    #bot.send_message(message.chat.id, 'Привет %s, ты написал мне /start' % message.from_user.username)

# deck = make_deck()
# print(deck)
print('Starting bot.....')
bot.polling()