# -*- coding: utf-8 -*-
import telebot

BOT_TOKEN = '449812079:AAHHnv4wl9Zdd4lZk5ZUQDmD5yDbgEYtF1I'
CHANNEL_NAME = '@testcanaltestcanaltestcanal'
chat_id = '-1001112215520'

bot = telebot.TeleBot(BOT_TOKEN)


def send_telegram(type, **kwargs):
    if type == 'call':
        bot.send_message(chat_id,
                         'Звонок\nИмя: {0}\nАдрес: {1}\nТелефон: {2}\nДата: {3}'.format(kwargs['name'],
                                                               kwargs['address'],
                                                               kwargs['phone'],
                                                               str(kwargs['order_date'])
                                                               )
                         )
    if type == 'order':
        elem_list = kwargs['elem_list']
        order = str()
        for attr in elem_list:
            order += '--------\nПродукт: {0}\nВес: {1} КГ\nСумма: {2} Р\n-------'.format(str(attr[0]), str(attr[1]), str(attr[2]))
        bot.send_message(chat_id,
                         'Заказ\nИмя: {0}\nАдрес: {1}\nТелефон: {2}\nДата заказа: {3}\nСумма заказа: {4} Р.\n{5}'.format(
                             kwargs['name'],
                             kwargs['address'],
                             kwargs['phone'],
                             str(kwargs['order_date']),
                             str(kwargs['order_sum']),
                             order)
                         )
