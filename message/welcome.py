def welcome(bot, update):
    text = "Приветики, @{0}!\n" \
           "Сразу пишу, что тебе нужно будет поговорить с @FromSi в личных сообщениях!\n\n" \
           "Мы все тут дружелюбные разработчики ^^\n" \
           "Из правил, ты, не должен скидывать ничего связанного с порнографией!\n" \
           "Скора дадим админку (мы любим равноправие).\n\n" \
           "Не стесняйся /help :3".format(update.message.new_chat_members[0].username)

    bot.send_message(chat_id=update.message.chat_id,
                     text=text)