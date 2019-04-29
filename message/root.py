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

names = {
    "FromSi": ["Влад", "Казахстан", ["Программирование", "Дрочка"], "Linux", ["Java", "Kotlin", "Python"]],
    "exynil": ["Максим", "Казахстан", ["Программирование", "3D моделирование"], "Linux", ["C#", "Python"]],
    "l33tpr09": ["l33tpr09", "Казахстан", ["Танцы", "Программирование"], "MacOS", ["JavaScript"]],
    "bexuma": ["Трактор", "Казахстан", ["Чтение", "Разработка ПО", "Прослушиваие инервью", "Конспектирование интервью"],
               "MacOS", ["C", "Ruby"]],
    "itnstr97": ["itnstr97", "Ukraine", ["Digital 3D", "GD", "Scripting", "Extreme vocals"], "Windows 8.1 x64",
                 ["C#", "CPP"]],
    "ArtMingo": ["Wise", "Ukraine", ["IT", "Photo", "Music", "Design"], "MacOS", ["JS", "C++"]],
    "ButerLord": ["Buter", "Kazakhstan", ["Программирование"], "Не все пробовал, пока винда", ["Python", "C++", "JS"]],
    "kruzenshtern2": [".@kruzenshtern2", ".Kz", [".CyberSec"], ".хз, Linux", [".python норм впренцепе"]],
    "chechenitza": ["Chechen Itza", "Kazakhstan", ["т"], "Арч линукс збс", ["С++"]],
    "kz12oleg12": ["Олег (snowball)", "Казахстан", ["Design"], "Пока нет любимой ОС", ["Java Script"]],
    "mnogoslonov": ["Banan", "Россия", ["IT", "Современное искусство", "Естественные науки"], "Linux/OS X",
                    ["Python", "Bash", "C"]],
    "ScreaMonhik": ["Дмитрий", "Украина", ["Пока игрульки", "Интересно программирование"], "Windows",
                    ["Swift", "React Native"]],
    "AquliaX": ["Andrew (Aquliax)", "Belarus", ["Games", "Programming"], "Windows", ["Java"]],
    "eduard_ilyaskin": ["Эдуард", "Казахстан", ["Музыка"], "MacOS", ["JS", "Dart"]]
}


def create_name(name, root=False):
    str = ""
    symbol = ""

    if root:
        str = f"├┬╸{name[0]}\n"
        symbol = "│"
    else:
        str = f"╭╸{name[0]}\n"

    str += symbol + "├┬╸Страна\n" + symbol + f"│╰─╸{name[1]}\n"
    str += symbol + "├┬╸Хобби\n"

    for i in range(len(name[2])):
        if len(name[2]) == (i + 1):
            str += symbol + f"│╰─╸{name[2][i]}\n"
        else:
            str += symbol + f"│├─╸{name[2][i]}\n"

    str += symbol + "├┬╸Любимая ОС\n" + symbol + f"│╰─╸{name[3]}\n"
    str += symbol + "├┬╸Любимые ЯП\n"

    for i in range(len(name[4])):
        if len(name[4]) == (i + 1):
            str += symbol + f"╹╰─╸{name[4][i]}\n"
        else:
            str += symbol + f"│├─╸{name[4][i]}\n"

    return str


def create_root():
    symbol = ""
    str = "╭╸Illuminati Inc.\n"

    for key, value in names.items():
        str += create_name(name=value, root=True)

    return str + "╹"


def name(bot, update, args):
    if names.get(args[0]) is not None:
        message = bot.send_message(chat_id=update.message.chat_id,
                                   text=create_name(name=names[args[0]]),
                                   reply_to_message_id=update.message.message_id)

        utils.clear.clear_message(bot, update, message)
    else:
        message = bot.send_message(chat_id=update.message.chat_id,
                                   text="Ошибка!\nТакого ника не существует в БД.",
                                   reply_to_message_id=update.message.message_id)

        utils.clear.clear_message(bot, update, message)


def root(bot, update):
    message = bot.send_message(chat_id=update.message.chat_id,
                               text=create_root(),
                               reply_to_message_id=update.message.message_id)

    utils.clear.clear_message(bot, update, message)
