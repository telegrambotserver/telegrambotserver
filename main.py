import telebot

bot = telebot.TeleBot("5286569426:AAGrMP-U7h7f1uUq658gwpH8PnPdE4-URAc")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == 'Пошол нахуй':
        bot.reply_to(message, "Охуел сам иди")
    elif message.text == 'Слава':
        bot.reply_to(message, "Слава натуральный гей, это сразу понятно")
    else:
	    bot.reply_to(message, "cам ты "+message.text+", пошол нахуй")


bot.polling(none_stop = True)
