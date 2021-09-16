from gamelib import make_deck
import telebot
key = '1765842295:AAH_Vj8ti5WSjsU5mUFS7U3tOY2AmCinkAY'
bot = telebot.TeleBot(key)

# deck = make_deck()
# print(deck)
print('Starting bot.....')
bot.polling()