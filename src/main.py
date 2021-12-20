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
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(eighth_form_handler)
    dp.add_handler(eighth_form)
    dp.add_handler(ninth_form_handler)
    dp.add_handler(ninth_form)
    dp.add_handler(tenth_form_handler)
    dp.add_handler(tenth_form)
    dp.add_handler(eleventh_form_handler)
    dp.add_handler(eleventh_form)
    dp.add_handler(week_handler)
    dp.add_handler(pokas_rasp_handler)
    dp.add_handler(MessageHandler(Filters.text, any_other_messages))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
