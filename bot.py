import os

from message.root import *
from message.roll import *
from message.help import *
from message.pin import *
from telegram.ext import *


def main():
    TOKEN = os.environ.get('TOKEN')
    NAME = os.environ.get('NAME')
    PORT = os.environ.get('PORT')

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('help', help, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('hroot', hroot, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('hroll', hroll, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('root', root, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('name', name, pass_args=True, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('roll', roll, pass_args=True, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler('pin', pin_reply_message, pass_job_queue=True))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()


if __name__ == '__main__':
    main()