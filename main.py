from datetime import datetime

import telebot
from telebot import types
from telebot.types import Message

from config_data.config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


# Обработка команды /help
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Ленина 1")
    btn2 = types.KeyboardButton("Оплата")
    btn3 = types.KeyboardButton("Картинка")
    btn4 = types.KeyboardButton("Гугл табличка")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!\n"
                          "Я бот - тестовое задание\n"
                          "Ты можешь использовать кнопки или написать в чат для проверки валидности даты\n"
                          "Жми /help если запутался\n"
                          "Удачи!".format(message.from_user), reply_markup=markup)


# Обработка команды /help
@bot.message_handler(commands=['help'])
def help_command(message: Message):
    bot.send_message(message.chat.id,
                     text='Кнопка Ленина 1 направит ссылку на Яндекс карты по этому адресу\n'
                          'Кнопка Оплата направит ссылку на оплату\n'
                          'Кнопка Картинка отправит картинку\n'
                          'Кнопка Гугл таблица отправит данные из гугл таблички\n'
                          'Напишите дату в формате дд.мм.гггг и я проверю её на валидность'.format(message.from_user))


# Обработка кнопок
@bot.message_handler(content_types=['text'])
def func(message: Message):
    if "Ленина 1" == message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Ссылка на карту!")
        bot.send_message(message.chat.id, text="https://yandex.ru/maps/216/zelenograd/house/ulitsa_lenina_1"
                                               "/Z04YdwBjSkcOQFtvfXV2eXhlbA==/?indoorLevel=1&ll=37.173328%2C55.978468"
                                               "&z=17.33")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)

    elif message.text == "Оплата":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Ссылка на оплату")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)

    elif message.text == "Картинка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Картинка")
        bot.send_photo(message.chat.id, open('images/cat.jpeg', 'rb'))
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)

    elif message.text == "Гугл табличка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Гугл табличка")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ленина 1")
        btn2 = types.KeyboardButton("Оплата")
        btn3 = types.KeyboardButton("Картинка")
        btn4 = types.KeyboardButton("Гугл табличка")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

# По условию, если текст был введён не с кнопки, то это дата. Переходим в блок валидатора даты
    else:
        try:
            if datetime.strptime(message.text, "%d.%m.%Y"):
                bot.send_message(message.chat.id, text="Дата корретная")
        except ValueError:
            bot.send_message(message.chat.id, text="Неверный формат даты!\n"
                                                   "Введите дату в формате дд.мм.гггг\n"
                                                   "обратите внимания, что числа должны быть разделены точкой")


bot.polling(none_stop=True)
