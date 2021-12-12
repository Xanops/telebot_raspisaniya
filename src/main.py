from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from token import TOKEN
from info import *


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://ip:port',  # Адрес прокси сервера
        # Опционально, если требуется аутентификация:
        # 'urllib3 proxy kwargs': {
        # 'assert_hostname': 'False',
        # 'cert_reqs': 'CERT_NONE'
        # 'username': 'user',
        # 'password': 'password'
        # }
    }
    updater = Updater(TOKEN, use_context=True,
                      request_kwargs=REQUEST_KWARGS)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, zatichka)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
