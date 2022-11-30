import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot Started...")


def startCommand(update, context):
    update.message.reply_text('Type something random to get started!')


def helpCommand(update, content):
    update.message.reply_text('If you need help! You should ask for it on Google!')


def handleMessage(update, context):
    text = str(update.message.text).lower()
    response = R.sampleRespones(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update:- {update} caused error {context.error}")


def main():
    update = Updater(keys.API_KEY, use_context=True)
    dp = update.dispatcher
    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(CommandHandler("help", helpCommand))
    dp.add_handler(MessageHandler(Filters.text, handleMessage))
    dp.add_error_handler(error)
    update.start_polling()
    update.idle()


main()
