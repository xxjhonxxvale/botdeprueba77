import os
import telegram
from telegram.ext import Updater, CommandHandler, updater

def Start(update, context):
    update.message.reply_text("Hola, otra vez :')")

def Help(update, context):
    update.message.reply_text('Usa /qr para generar un codigo qr')

if __name__ == '__main__':

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('Start', Start))

    dp.add_handler(CommandHandler('Help', help))


    updater.start_polling()
    updater.idle()

