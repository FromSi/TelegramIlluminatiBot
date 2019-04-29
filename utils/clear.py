import time
from telegram.ext import *


@run_async
def clear_message(bot, update, message):
    timer_base = timer_live = 30
    icons = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]

    while timer_live != 0:
        time.sleep(1)

        timer_live -= 1
        message_text = f"\n\n{icons[(timer_base - timer_live) % 12]} Удаление через {timer_live}"

        bot.edit_message_text(chat_id=update.message.chat_id,
                              text=message.text + message_text,
                              message_id=message.message_id)

    bot.deleteMessage(chat_id=update.message.chat_id,
                      message_id=update.message.message_id)

    bot.deleteMessage(chat_id=update.message.chat_id,
                      message_id=message.message_id)