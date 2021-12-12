def start(update, context):
    update.message.reply_text(
        "Привет! Я бот, который присылает расписание для учеников"
        " Университетского лицея 1523 Предуниверситария НИЯУ МИФИ.")


def help(update, context):
    update.message.reply_text("Я пока не умею помогать...")


def zatichka(update, context):
    update.message.reply_text("Извините, я пока что не функционален.")
