import telebot
from flask import flask, request
import os
TOKEN = "872259319:AAHPKA8Csh6ERD0RMLN90zZZPzluFqoFI88"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chatid=message.chat.id

    bot.send_message(chatid, "Hola, /clikeame")

@bot.message_handler(commands=['clikeame'])
def uno(message):
    chatid=message.chat.id
        
    bot.send_message(chatid, "En primer primer lugar, aca también sí hay stickers y están más ordenados. Agregalos!")
    bot.send_message(chatid, "https://t.me/addstickers/sebaspack")
    bot.send_message(chatid, "https://t.me/addstickers/Meme_stickers")
    bot.send_message(chatid, "https://t.me/addstickers/CDJMeme")
    bot.send_message(chatid, "/continua")

@bot.message_handler(commands=['continua'])
def dos(message):
    chatid=message.chat.id
        
    bot.send_message(chatid, "Incluso hay stickers animados")
    bot.send_message(chatid, "Intenta mandar el emoji de un corazón")


@bot.message_handler(regexp="❤")
def tres(message):
    chatid=message.chat.id
    bot.send_message(chatid, "Muy bien, ahora investiga el resto de emojis que son animados. Mientas, explora algunos packs de stickers animados")
    bot.send_message(chatid, "https://t.me/addstickers/HotCherry")
    bot.send_message(chatid, "https://t.me/addstickers/CorgiMuffin")
    bot.send_message(chatid, "/excelente !!")

@bot.message_handler(commands=['excelente'])
def cuatro(message):
    chatid=message.chat.id

    bot.send_message(chatid, "Pues existen los grupos y los canales")
    bot.send_message(chatid, "En los grupos cualquiera puede hablar, como en @excelhechofacil")
    bot.send_message(chatid, "Mientras que en los canales sólo recibes los mensajes, como en @zukulentosmemes")
    bot.send_message(chatid, "Para buscar más grupos y canales entra a @ListaTelegram, @listadogram o @DirectorioTelegram, donde están filtrados por tópico")
    bot.send_message(chatid, "/genial!")


@bot.message_handler(commands=['genial'])
def cinco(message):
    chatid=message.chat.id

    bot.send_message(chatid, "Tambien existen los bots (como el que estás hablando ahora).")
    bot.send_message(chatid, "Estos son seguros y pueden hacer infinidad de cosas, por ejemplo, @getmediabot descarga cualquier cancion que le escribamos, @memerator_bot genera memes simples sólo a partir de una imagen, como la siguiente")

        
    bot.send_photo(chatid, open( './temp/meme.png', 'rb'))

    bot.send_message(chatid, "Un par de últimas cosas. /Dime")

@bot.message_handler(commands=['Dime'])
def seis(message):
    chatid=message.chat.id

    bot.send_message(chatid, "Todo el contenido que recibas está en una nube y puedes siempre volver a descargarlo en caso de borrarlo")
    bot.send_message(chatid, "Para borrar el caché sigue el siguiente tutorial")

    bot.send_video(chatid, open( './temp/vidcache.mp4', 'rb'))    
    
    bot.send_message(chatid, "Y por último, se pueden guardar gifs, mira este pequeño tutorial :3")

    bot.send_video(chatid, open( './temp/vidgif.mp4', 'rb'))

    bot.send_message(chatid, "Intenta!")

    bot.send_video(chatid, open( './temp/fry.mp4', 'rb'))

    bot.send_message(chatid, "Y eso es todo, bienvenido oficialmente a Telegram")

@bot.message_handler(commands=['foto'])
def send_photo(message):
    chatid=message.chat.id
        
    bot.send_message(chatid, "wolas ")

    bot.send_photo(chatid, open( './temp/hola.png', 'rb'))

print("Ejecutandose")
#bot.polling()
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

