import random, utils.clear


def roll(bot, update, args):
    answer = ""

    if len(args) == 3:
        n1 = min(int(args[0]), int(args[1]))
        n2 = max(int(args[0]), int(args[1]))
        n3 = 30

        if int(args[2]) < n3:
            n3 = int(args[2])

        answer += f"Вы получили {n3} рандомных чисел!\n(От {n1} – до {n2})\n\n"

        for i in range(n3):
            answer += f"{i + 1}: {random.randint(n1, n2)}\n"
    elif len(args) == 2:
        n1 = min(int(args[0]), int(args[1]))
        n2 = max(int(args[0]), int(args[1]))
        answer += f"Вам выпало число {random.randint(n1, n2)}.\n(От {n1} – до {n2})"
    elif len(args) == 1:
        answer += f"Вам выпало число {random.randint(0, int(args[0]))}.\n(От 1 – до {args[0]})"
    else:
        answer += "Не верная команда!\nОбратитесь в /help"

    message = bot.send_message(chat_id=update.message.chat_id,
                               text=answer,
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message)
