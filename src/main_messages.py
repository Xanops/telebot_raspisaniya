from telegram import ReplyKeyboardMarkup


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот, который присылает расписание для учеников "
        "Университетского лицея 1523 Предуниверситария НИЯУ МИФИ. "
        "Выберете пожалуйста цифру вашего класса:", reply_markup=start_markup)


numbers_of_forms_reply_keyboard = [["8 класс", "9 класс"],
                                   ["10 класс", "11 класс"]]

start_markup = ReplyKeyboardMarkup(numbers_of_forms_reply_keyboard, one_time_keyboard=True)


def any_other_messages(update, context):
    update.message.reply_text("Извините, мой функционал включает только информирование о расписании.")


def pokas_rasp(update, context):
    update.message.reply_text("лол, фиг тебе")


def stop(update, context):
    update.message.reply_text("Ошибка")
