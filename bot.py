import os

os.environ['TOKEN']
from telegram import Update
from telegram.ext import dispatcher, Updater, CommandHandler, MessageHandler, Filters

# Configuramos el comando start para enviar un mensaje de bienvenida
def start(update, context):

    update.message.reply_text('Hola humano!')

def echo(update, context):
    # Configuramos para enviar un mensaje con el texto que envió el usuario, aquí es donde va a ir toda la lógica de nuestro bot
    # Es decir... la instruccion que hace que se repita todo lo que envie de mensaje que no sea un comando
    update.message.reply_text(update.message.text)


if __name__ == '__main__' :  #significa que el programa iniciara a partir de aqui
    
    # Creamos el Updater y le pasamos el token de nuestro bot. Este se encargará de manejar las peticiones de los usuarios.
    # El 'udpater' es una variable
    updater = Updater(token='TOKEN', use_context=True)

    # Obtenemos el Dispatcher para crear los comandos
    dp = updater.dispatcher
    
    # Creamos el comando /start y definimos que se ejecute este mismo método
    dp.add_handler(CommandHandler('start', start))

    # De no ejecutarse ninguno de los anteriores asumimos que el usuario escribió algo y ejecutamos el método echo que nos va a permitir obtener los campos de las búsquedas del usuario
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

#1 Se declaran los comandos dentro del __Main__
#2 Se declaran las accioden del comando antes del __Main__
