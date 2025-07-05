import telebot

API_token = '7858814635:AAGa6pJYQs0-WE-pkOX9gZDQcVuhKPk5zIk'

bot = telebot.TeleBot(API_token)

@bot.message_handler(func=lambda message: True)
def hi(message):
    print('hui', message.from_user.id)

bot.send_message(5608629096, 'PRIVET')

bot.polling()