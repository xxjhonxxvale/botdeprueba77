
from telegram import Update
from telegram.ext import dispatcher, Updater, CommandHandler

# def start(udpate, context):
def start(update, context):

    update.message.reply_text('Hola humano!')



if __name__ == '__main__' :
    
    updater = Updater(token='2097638862:AAEmflVzqB8L6ux6r02hDm10TMhpkVNSTVs', use_context=True)

    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext


# def hola(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Kenny afina pistolas {update.effective_user.first_name}')


# updater = Updater('2097638862:AAEmflVzqB8L6ux6r02hDm10TMhpkVNSTVs', use_context=True)

# updater.dispatcher.add_handler(CommandHandler('hola', hola))

# updater.start_polling()
# updater.idle()

