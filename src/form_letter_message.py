from telegram import ReplyKeyboardMarkup
import json


# Запись в json номера класса и вопрос о букве 8ых классов
def eighth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[0]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=eighth_form_letters)
    return "week question"


# Запись в json номера класса и вопрос о букве 9ых классов
def ninth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[0]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=ninth_form_letters)
    return "week question"


# Запись в json номера класса и вопрос о букве 10ых классов
def tenth_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[:2]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=tenth_form_letters)
    return "week question"


# Запись в json номера класса и вопрос о букве 11ых классов
def eleventh_form_letter(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["clas"] = update.message.text[:2]
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете букву класса:", reply_markup=eleventh_form_letters)
    return "week question"


# Экземпляр клавиатуры букв 8ых классов
eighth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1"], ["М2", "Н2", "О2"]], one_time_keyboard=True)

# Экземпляр клавиатуры букв 9ых классов
ninth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                         one_time_keyboard=True)

# Экземпляр клавиатуры букв 10ых классов
tenth_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"], ["С"]],
                                         one_time_keyboard=True)

# Экземпляр клавиатуры букв 11ых классов
eleventh_form_letters = ReplyKeyboardMarkup([["М1", "Н1", "О1", "П1", "Р1"], ["М2", "Н2", "О2", "П2", "Р2"]],
                                            one_time_keyboard=True)
