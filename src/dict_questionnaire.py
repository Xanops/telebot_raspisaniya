from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler
from week_question import *
from form_letter_message import *
from main_messages import pokas_rasp, stop

# Обработчик чётности недели
week_handler = MessageHandler(Filters.text(["М1", "М2", "Н1", "Н2", "О1", "О2", "П1", "П2", "Р1", "Р2", "С", ]),
                              week_question)

# Обработчик вывода расписания
pokas_rasp_handler = MessageHandler(Filters.text(["чётная", "Чётная", "четная", "Четная",
                                                  "нечётная", "Нечётная", "нечетная", "Нечетная"]), pokas_rasp)

# Словарь последовательности опроса
posledovatelnost_oprosa = {"week question": [week_handler],
                           2: [pokas_rasp_handler]}

# Обработчик буквы 8ых классов
eighth_form_handler = MessageHandler(Filters.text(["8 класс", "8"]), eighth_form_letter)
# Последовательный обработчик-диалог для 8ых классов
eighth_form = ConversationHandler(entry_points=[eighth_form_handler],
                                  states=posledovatelnost_oprosa,
                                  fallbacks=[CommandHandler('cancel', stop)])

# Обработчик буквы 9ых классов
ninth_form_handler = MessageHandler(Filters.text(["9 класс", "9"]), ninth_form_letter)
# Последовательный обработчик-диалог для 9ых классов
ninth_form = ConversationHandler(entry_points=[ninth_form_handler],
                                 states=posledovatelnost_oprosa,
                                 fallbacks=[CommandHandler('cancel', stop)])

# Обработчик буквы 10ых классов
tenth_form_handler = MessageHandler(Filters.text(["10 класс", "10"]), tenth_form_letter)
# Последовательный обработчик-диалог для 10ых классов
tenth_form = ConversationHandler(entry_points=[tenth_form_handler],
                                 states=posledovatelnost_oprosa,
                                 fallbacks=[CommandHandler('cancel', stop)])

# Обработчик буквы 11ых классов
eleventh_form_handler = MessageHandler(Filters.text(["11 класс", "11"]), eleventh_form_letter)
# Последовательный обработчик-диалог для 11ых классов
eleventh_form = ConversationHandler(entry_points=[eleventh_form_handler],
                                    states=posledovatelnost_oprosa,
                                    fallbacks=[CommandHandler('cancel', stop)])

# Словарь, который нужен для вызова обработчиков-диалогов после выбора номера класса
starting_dict = {
    "8 класс": [eighth_form],
    "9 класс": [ninth_form],
    "10 класс": [tenth_form],
    "11 класс": [eleventh_form]
}

