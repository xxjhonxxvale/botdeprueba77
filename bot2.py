import os

from telegram.ext import Updater, CommandHandler, updater

def Start(update, context):
    update.message.reply.text("Hola, otra vez :')")

def Help(update, context):
    update.message.reply.text('Usa /qr para generar un codigo qr')

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('Start', Start))

    dp.add_handler(CommandHandler('Help', help))


    updater.start_polling()
    updater.idle()

