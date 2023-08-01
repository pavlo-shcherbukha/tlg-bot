# bot in telegram

from datetime import datetime,timedelta
#import json
#import logging
#import datetime
import sys
import traceback
import os
#import time
import telebot
from telebot import types

bot_token='6355593383:AAFOxXokjJY061YaXbbe5RRp8rX9nOVurpA'
bot = telebot.TeleBot(bot_token)


"""
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привіт":
        bot.send_message(message.from_user.id, "Привіт !!!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши мені привіт")
    else:
        bot.send_message(message.from_user.id, "Ну не пойняв я. Напиши /help.")



"""

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Як тебя звати?")
        bot.register_next_step_handler(message, get_name); #потом функція get_name
    elif message.text.upper() == 'ДА':
        bot.send_message(message.from_user.id, 'Приємно познайомитися!!! ' + message.from_user.full_name )
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаєм фам
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Напиши прізвище?')
    bot.register_next_step_handler(message, get_surname )

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Скільки тобі років?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    ok=True
    while ok == True: #перевіряємо вік
        try:
             age = int(message.text) # перевіряєм чи є вік цифра
             ok=False
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, будь ласка');
            ok=False
    bot.send_message(message.from_user.id, 'Тобі '+str(age)+' років, тебе звати '+name+' '+surname+'?')



if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)