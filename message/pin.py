import utils.clear


def pin_reply_message(bot, update, job_queue):
    bot.pin_chat_message(chat_id=update.message.chat_id,
                         message_id=update.message.reply_to_message.message_id)

    message = bot.send_message(chat_id=update.message.chat_id,
                               text="Сделяль :3",
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 10, job_queue)
