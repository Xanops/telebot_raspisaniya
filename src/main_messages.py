from telegram import ReplyKeyboardMarkup
from excel import get_rasp
import json


# Приветствие
def start(update, context):
    update.message.reply_text(
        "Привет! Я бот, который присылает расписание для учеников "
        "Университетского лицея 1523 Предуниверситария НИЯУ МИФИ. "
        "Выберете пожалуйста цифру вашего класса:", reply_markup=start_markup)


numbers_of_forms_reply_keyboard = [["8 класс", "9 класс"],          # Разметка клавиатуры классов
                                   ["10 класс", "11 класс"]]

start_markup = ReplyKeyboardMarkup(numbers_of_forms_reply_keyboard, one_time_keyboard=True)  # Создание экземпляра
                                                                                             # клавиатуры классов


# Обраьотка остальных сообщений
def any_other_messages(update, context):
    update.message.reply_text("Извините, мой функционал включает только информирование о расписании. "
                              "Выберете действие на клавиатуре или введите команду /start для начала диалога.")


# Обработать введённые ответы и вывести расписание
def pokas_rasp(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    clas = data["clas"]
    letter = data["letter"]
    if update.message.text in ["чётная", "Чётная", "четная", "Четная"]:
        week = "чет"
    elif update.message.text in ["нечётная", "Нечётная", "нечетная", "Нечетная"]:
        week = "нечет"
    update.message.reply_text(get_rasp(week, clas, letter), reply_markup=ReplyKeyboardMarkup([["Начать"]],
                                                                                             one_time_keyboard=True))


# Функция при ошибке последовательности диалога
def stop(update, context):
    update.message.reply_text("Ошибка")
