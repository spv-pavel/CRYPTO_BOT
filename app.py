import telebot


TOKEN = '6293751402:AAEa8tUjJfcslx6tDaHcuDWXL2sGjI3t9Oc'


bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')


bot.polling()
