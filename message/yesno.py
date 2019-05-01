import random
import utils.clear


def yesno(bot, update, args, job_queue):
    answers = ["да", "нет", "спорно", "больше да, чем нет", "больше нет, чем да"]
    text = "На вопрос:\n"

    for arg in args:
        text += arg + " "

    text += f"\n\nЯ отвечу, что {answers[random.randint(0, 4)]}!"

    message = bot.send_message(chat_id=update.message.chat_id,
                               text=text,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 10, job_queue)
