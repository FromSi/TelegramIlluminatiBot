import utils.clear

help_message = '''
Список мне понятных команд

/hroot 
Объясню команды /root и /name

/hroll
Объясню команду /roll

/pin
Закреплю сообщение

/root 
Древо чатика

/name {Ник пользователя}
Древо милашки

/roll {одно, два или три числа}
Придумаю рандомные числа
'''

help_message_root = '''
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


def help(bot, update, job_queue):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 60, job_queue)


def hroot(bot, update, job_queue):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message_root,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 60, job_queue)


def hroll(bot, update, job_queue):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=help_message_roll,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 60, job_queue)
