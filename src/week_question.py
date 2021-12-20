from telegram import ReplyKeyboardMarkup


def week_question(update, context):
    update.message.reply_text("Выберете неделю:", reply_markup=ReplyKeyboardMarkup([["Чётная", "Нечётная"]],
                                                                                   one_time_keyboard=True))
    return 2
