import os
import telegram
from telegram import Update, bot
from telegram.ext import Updater, CommandHandler, ConversationHandler

def start(update, context):
    update.message.reply_text("Hola, otra vez :')")

def help(update, context):
    update.message.reply_text('Usa /qr para generar un codigo qr')

def qr_command_handler(update, context):
    update.message.reply_text('Inviame el texto para generar el qr')

if __name__ == '__main__':

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('Start', start))

    dp.add_handler(CommandHandler('Help', help))

    dp.add_handler(ConversationHandler(
        entry_points=[
            ConversationHandler('qr', qr_command_handler)
        ],

        states={},

        fallbacks=[]

    ))


    updater.start_polling()
    updater.idle()

