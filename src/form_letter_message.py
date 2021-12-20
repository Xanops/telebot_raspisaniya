from telegram import ReplyKeyboardMarkup


def eighth_form_letter(update, context):
    update.message.reply_text("Выберете букву класса:", reply_markup=eighth_form_letters)
    return "week question"


def ninth_form_letter(update, context):
    update.message.reply_text("Выберете букву класса:", reply_markup=ninth_form_letters)
    return "week question"


def tenth_form_letter(update, context):
    update.message.reply_text("Выберете букву класса:", reply_markup=tenth_form_letters)
    return "week question"


def eleventh_form_letter(update, context):
    update.message.reply_text("Выберете букву класса:", reply_markup=eleventh_form_letters)
    return "week question"


eighth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1"], ["М2", "Н2", "О2"]], one_time_keyboard=True)

ninth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                         one_time_keyboard=True)

tenth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"], ["С"]],
                                         one_time_keyboard=True)

eleventh_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                            one_time_keyboard=True)
