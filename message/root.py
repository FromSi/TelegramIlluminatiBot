"""
╭╸Влад
├┬╸Страна
│╰─╸Казахстан
├┬╸Хобби
│├─╸Программирование
│╰─╸Дрочка
├┬╸Любимая ОС
│╰─╸Linux
├┬╸Любимые ЯП
│├─╸Java
│├─╸Kotlin
╹╰─╸Python
"""

import utils.clear
from sql.queries import get_user_annotation, get_users


def create_name(annotation, root=False):
    str = ""
    symbol = ""
    user = get_user_annotation(annotation)[0]

    if root:
        str = f"├┬╸{user.name}\n"
        symbol = "│"
    else:
        str = f"╭╸{user.name}\n"

    str += symbol + "├┬╸Страна\n" + symbol + f"│╰─╸{user.country}\n"
    str += symbol + "├┬╸Хобби\n"

    if user.hobby_one is not None and user.hobby_two is not None:
        str += symbol + f"│├─╸{user.hobby_one}\n"
    elif user.hobby_one is not None:
        str += symbol + f"│╰─╸{user.hobby_one}\n"

    if user.hobby_two is not None and user.hobby_three is not None:
        str += symbol + f"│├─╸{user.hobby_two}\n"
    elif user.hobby_two is not None:
        str += symbol + f"│╰─╸{user.hobby_two}\n"

    if user.hobby_three is not None and user.hobby_four is not None:
        str += symbol + f"│├─╸{user.hobby_three}\n"
    elif user.hobby_three is not None:
        str += symbol + f"│╰─╸{user.hobby_three}\n"

    if user.hobby_four is not None and user.hobby_five is not None:
        str += symbol + f"│├─╸{user.hobby_four}\n"
        str += symbol + f"│├─╸{user.hobby_five}\n"
    elif user.hobby_four is not None:
        str += symbol + f"│╰─╸{user.hobby_four}\n"

    str += symbol + "├┬╸Любимая ОС\n" + symbol + f"│╰─╸{user.favorite_os}\n"
    str += symbol + "├┬╸Любимые ЯП\n"

    if user.language_one is not None and user.language_two is not None:
        str += symbol + f"│├─╸{user.language_one}\n"
    elif user.language_one is not None:
        str += symbol + f"╹╰─╸{user.language_one}\n"

    if user.language_two is not None and user.language_three is not None:
        str += symbol + f"│├─╸{user.language_two}\n"
    elif user.language_two is not None:
        str += symbol + f"╹╰─╸{user.language_two}\n"

    if user.language_three is not None and user.language_four is not None:
        str += symbol + f"│├─╸{user.language_three}\n"
    elif user.language_three is not None:
        str += symbol + f"╹╰─╸{user.language_three}\n"

    if user.language_four is not None and user.language_five is not None:
        str += symbol + f"│├─╸{user.language_four}\n"
        str += symbol + f"╹├─╸{user.language_five}\n"
    elif user.language_four is not None:
        str += symbol + f"╹╰─╸{user.language_four}\n"

    return str


def create_root():
    str = "╭╸Illuminati Inc.\n"

    for user in get_users():
        str += create_name(annotation=user.annotation, root=True)

    return str + "╹"


def name(bot, update, args, job_queue):
    if get_user_annotation(args[0]) is not None:
        message = bot.send_message(chat_id=update.message.chat_id,
                                   text=create_name(annotation=args[0]),
                                   reply_to_message_id=update.message.message_id)

        utils.clear.clear_message(bot, update, message, 20, job_queue)
    else:
        message = bot.send_message(chat_id=update.message.chat_id,
                                   text="Ошибка!\nТакого ника не существует в БД.",
                                   reply_to_message_id=update.message.message_id)

        utils.clear.clear_message(bot, update, message, 10, job_queue)


def root(bot, update, job_queue):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=create_root(),
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message, 60, job_queue)
