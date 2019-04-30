from telegram.ext import *


@run_async
def clear_message(bot, update, message, seconds, job_queue):
    def delete_message(bot, job):
        bot.delete_message(chat_id=update.message.chat_id,
                           message_id=update.message.message_id)

        bot.delete_message(chat_id=update.message.chat_id,
                           message_id=message.message_id)

    message_text = f"\n\n🕑 Удаление сообщений через {seconds}"

    bot.edit_message_text(chat_id=update.message.chat_id,
                          text=message.text + message_text,
                          message_id=message.message_id)

    job_queue.run_once(delete_message, seconds)
