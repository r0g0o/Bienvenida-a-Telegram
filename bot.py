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
    update.message.reply_text('Hola, mundo')
    update.message.reply_text('Hola, /clikeame')
'''
def uno(update, context):
    update.message.reply_text('En primer primer lugar, aca también sí hay stickers y están más ordenados. Agregalos!')
    update.message.reply_text('https://t.me/addstickers/sebaspack')
    update.message.reply_text('https://t.me/addstickers/Meme_stickers')
    update.message.reply_text('https://t.me/addstickers/CDJMeme')
    update.message.reply_text('/continua')
    
def dos(update, context):
    update.message.reply_text('Incluso hay stickers animados')
    update.message.reply_text('Intenta mandar el emoji de un corazón')
    
def tres(update, context):
    update.message.reply_text('Muy bien, luego investiga el resto de emojis que son animados. Mientas, explora algunos packs de stickers animados')
    update.message.reply_text('https://t.me/addstickers/HotCherry')
    update.message.reply_text('https://t.me/addstickers/CorgiMuffin')
    update.message.reply_text('/excelente !!')
'''

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
    dp.add_handler(CommandHandler("start", start))"""
    dp.add_handler(CommandHandler("clickeame", uno))
    dp.add_handler(CommandHandler("continua", dos))
    dp.add_handler(CommandHandler("❤", tres))"""

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




