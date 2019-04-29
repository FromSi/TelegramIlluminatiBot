import utils.clear

help_message = '''
Команда для помощи в поиске команды.

/help
Помощь

/hroot 
Помощь по командам /root и /name

/root 
Полное древо людей

/name {Ник пользователя}
Древо пользователя

/roll {одно, для или три числа}
Генерация рандомных чисел

/hroll
Помощь по команде /roll
'''

help_message_root = '''
Команда для получения древа чата.

Показать весь корень:
/root

Список древа пользователей:
(Ссыдки на пользвателя телеграм, без @)
/name FromSi
/name exynil
/name l33tpr09
/name bexuma
/name itnstr97
/name ArtMingo
/name ButerLord
/name kruzenshtern2
/name chechenitza
/name kz12oleg12
/name mnogoslonov
/name ScreaMonhik
/name AquliaX
/name eduard_ilyaskin
'''

help_message_roll = '''
Команда для получения рандомных чисел.

/roll 99
Рандомное число 1..99

/roll 5 10
Рандомное число 5..10

/roll 5 10 30
30 рандомных чисел 5..10
'''


def help(bot, update):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message)


def hroot(bot, update):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message_root,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message)


def hroll(bot, update):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message_roll,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message)
