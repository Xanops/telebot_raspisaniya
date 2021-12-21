from telegram import ReplyKeyboardMarkup
import json


# Запись в json буквы класса и вопрос о чётности недели
def week_question(update, context):
    with open('value.json', 'r') as f:
        data = json.load(f)
    data["letter"] = update.message.text
    with open('value.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    update.message.reply_text("Выберете неделю:", reply_markup=ReplyKeyboardMarkup([["Чётная", "Нечётная"]],
                                                                                   one_time_keyboard=True))
    return 2
