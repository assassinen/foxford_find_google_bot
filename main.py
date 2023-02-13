import telebot
token = '6040475385:AAHLM_N2C2Dz_JUfQ4L6yqrAHi6z3_vpYWo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот! Я умею искать информацию в интернете за тебя. '
                                      'Напиши свой запрос в сообщении ниже.')


@bot.message_handler(content_types='text')
def message_reply(message):
    text = message.json.get('text')
    answer = f'https://google.com/?q={"+".join(text.split())}'
    bot.send_message(message.chat.id, answer)


bot.polling()
