from message.root import *
from message.roll import *
from message.help import *
from telegram.ext import *


index_thread = 1


def index_get():
    global index_thread

    if index_thread > 100:
        index_thread = 1
    else:
        index_thread += 1

    return index_thread


def main():
    updater = Updater(token='TOKEN')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('hroot', hroot))
    dispatcher.add_handler(CommandHandler('hroll', hroll))
    dispatcher.add_handler(CommandHandler('root', root))
    dispatcher.add_handler(CommandHandler('name', name, pass_args=True))
    dispatcher.add_handler(CommandHandler('roll', roll, pass_args=True))

    updater.start_polling()


if __name__ == '__main__':
    main()