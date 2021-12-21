from telegram import ReplyKeyboardMarkup
import json


def eighth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[0]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=eighth_form_letters)
    return "week question"


def ninth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[0]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=ninth_form_letters)
    return "week question"


def tenth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[:2]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=tenth_form_letters)
    return "week question"


def eleventh_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[:2]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=eleventh_form_letters)
    return "week question"


eighth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1"], ["М2", "Н2", "О2"]], one_time_keyboard=True)

ninth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                         one_time_keyboard=True)

tenth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"], ["С"]],
                                         one_time_keyboard=True)

eleventh_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                            one_time_keyboard=True)
