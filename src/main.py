from telegram.ext import Updater
from bot_token import bot_token
from main_messages import *
from dict_questionnaire import *


def main():
    # Создаём объект updater.
    updater = Updater(bot_token, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(MessageHandler(Filters.text("Начать") | Filters.command("start"), start))  # Приветственный обработчик
    dp.add_handler(eighth_form_handler)     # Обработчик сообщений номера 8 класса
    dp.add_handler(eighth_form)             # Последовательный обработчик-диалог сообщений для 8 класса
    dp.add_handler(ninth_form_handler)      # Обработчик сообщений номера 9 класса
    dp.add_handler(ninth_form)              # Последовательный обработчик-диалог сообщений для 9 класса
    dp.add_handler(tenth_form_handler)      # Обработчик сообщений номера 10 класса
    dp.add_handler(tenth_form)              # Последовательный обработчик-диалог сообщений для 10 класса
    dp.add_handler(eleventh_form_handler)   # Обработчик сообщений номера 11 класса
    dp.add_handler(eleventh_form)           # Последовательный обработчик-диалог сообщений для 11 класса
    dp.add_handler(week_handler)            # Обработчик чётности недели
    dp.add_handler(pokas_rasp_handler)      # Обработчик для вывода расписания
    dp.add_handler(MessageHandler(Filters.text, any_other_messages))    # Обработчик остальных сообщений
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
