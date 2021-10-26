from telegram.ext import Updater, CommandHandler, updater

def Start(update, context):
    update.message.reply.text("Hola, otra vez :')")

def Help(update, context):
    update.message.reply.text('Usa /qr para generar un codigo qr')

if __name__ == '__main__':

    updater = Updater(token='2097638862:AAEmflVzqB8L6ux6r02hDm10TMhpkVNSTVs', use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('Start', Start))

    dp.add_handler(CommandHandler('Help', help))


    updater.start_polling()
    updater.idle()

