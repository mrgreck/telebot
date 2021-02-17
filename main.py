import telebot

from config import TOCEN, keys
from extensions import ConvertionException,Convert


bot = telebot.TeleBot(TOCEN)



@bot.message_handler(commands=['start','help'])
def help(message:telebot.types.Message):
       text = 'Для того чтобы пользоваться этим ботом вам необходива \n' \
              'написать сообщение в следующем формате:\n' \
              '<имя валюты> <в какую валюту перевести> <количество валюты>\n' \
              'Для получения списка всех доступных валют: /value'
       bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['value'])
def value(message:telebot.types.Message):
       text = 'Доступные валюты:'

       for k in keys.keys():
              text = '\n'.join((text, k, ))

       bot.send_message(message.chat.id, text)

@bot.message_handler(content_types='text')
def convert(message:telebot.types.Message):


       try:
              v = message.text.split(' ')

              if len(v) < 3:
                     raise ConvertionException('Слишком мало параметров.')

              if len(v) > 3:
                     raise ConvertionException('Слишком много параметров.')

              base, symbold, amount = v

              value = Convert.get_price(base = base, symbold = symbold, amount = amount)
       except ConvertionException as e:
              bot.send_message(message.chat.id, f'Ошибка пользователя: {e}')
       except Exception as e:
              bot.send_message(message.chat.id, f'Не возможно оброботать сообщение: {e}')

       else:
              text = f'Цена {amount} {base} в {symbold}: {value}'
              bot.send_message(message.chat.id,text)





bot.polling()




