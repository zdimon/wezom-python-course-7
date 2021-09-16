from gamelib import make_deck
import telebot
key = '1765842295:AAH_Vj8ti5WSjsU5mUFS7U3tOY2AmCinkAY'
bot = telebot.TeleBot(key)


@bot.message_handler(commands=['start'])
def start_message(message):
    #print(message)
    #print(message.from_user.username)
    bot.send_message(message.chat.id, 'Привет %s, ты написал мне /start' % message.from_user.username)

# deck = make_deck()
# print(deck)
print('Starting bot.....')
bot.polling()