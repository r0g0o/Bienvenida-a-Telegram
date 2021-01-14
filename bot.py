import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '872259319:AAHPKA8Csh6ERD0RMLN90zZZPzluFqoFI88'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola, /clickeame')

def uno(update, context):
    update.message.reply_text('En primer primer lugar, aca también sí hay stickers y están más ordenados. Agregalos!')
    update.message.reply_text('https://t.me/addstickers/sebaspack')
    update.message.reply_text('https://t.me/addstickers/Meme_stickers')
    update.message.reply_text('https://t.me/addstickers/CDJMeme')
    update.message.reply_text('/continua')
    
def dos(update, context):
    update.message.reply_text('Incluso hay stickers animados')
    update.message.reply_text('https://t.me/addstickers/HotCherry')
    update.message.reply_text('https://t.me/addstickers/CorgiMuffin')
    update.message.reply_text('/excelente !!') 

def tres(update, context):
    update.message.reply_text('Pues existen los grupos y los canales')
    update.message.reply_text('En los grupos cualquiera puede hablar, como en @excelhechofacil') 
    update.message.reply_text('Mientras que en los canales sólo recibes los mensajes, como en @zukulentosmemes') 
    update.message.reply_text('Para buscar más grupos y canales entra a @ListaTelegram, @listadogram o @DirectorioTelegram, donde están filtrados por tópico')
    update.message.reply_text('/genial !')
    
def cuatro(update, context):
    update.message.reply_text('Tambien existen los bots (como el que estás hablando ahora).')
    update.message.reply_text('Estos son seguros y pueden hacer infinidad de cosas, por ejemplo, @getmediabot descarga cualquier cancion que le escribamos, @memerator_bot genera memes simples sólo a partir de una imagen, como la siguiente')
    update.message.reply_text('*foto')
    update.message.reply_text('Un par de últimas cosas. /Dime')
    
def cinco(update, context):
    update.message.reply_text('Todo el contenido que recibas está en una nube y puedes siempre volver a descargarlo en caso de borrarlo')
    update.message.reply_text('Para borrar el caché sigue el siguiente tutorial')
    update.message.reply_text('*cargando vids*')
    update.message.reply_text('*video')
    update.message.reply_text('Y por último, se pueden guardar gifs, mira este pequeño tutorial :3')
    update.message.reply_text('*otro vid')
    update.message.reply_text('Intenta!')
    update.message.reply_text('*último vid')
    update.message.reply_text('Y eso es todo, esta es mi bienvenida (no) oficial a Telegram')
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("clickeame", uno))
    dp.add_handler(CommandHandler("continua", dos))
    dp.add_handler(CommandHandler("excelente", tres))
    dp.add_handler(CommandHandler("genial", cuatro))
    dp.add_handler(CommandHandler("dime", cinco))



    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://bienvenidatelegram.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()




