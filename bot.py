import telebot

bot = telebot.TeleBot("872259319:AAHPKA8Csh6ERD0RMLN90zZZPzluFqoFI88")

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


    meme1=open('/Users/fncg6/OneDrive/Escritorio/pruebas programar/Bot Telegram/temp/meme.png','rb')
    bot.send_photo(chatid, meme1)

    bot.send_message(chatid, "Un par de últimas cosas. /Dime")


@bot.message_handler(commands=['Dime'])
def seis(message):
    chatid=message.chat.id

    bot.send_message(chatid, "Todo el contenido que recibas está en una nube y puedes siempre volver a descargarlo en caso de borrarlo")
    bot.send_message(chatid, "Para borrar el caché sigue el siguiente tutorial")

    vidcache=open('/Users/fncg6/OneDrive/Escritorio/pruebas programar/Bot Telegram/temp/vidcache.mp4','rb')
    bot.send_video(chatid, vidcache)    
    
    bot.send_message(chatid, "Y por último, se pueden guardar gifs, mira este pequeño tutorial :3")

    vidgif=open('/Users/fncg6/OneDrive/Escritorio/pruebas programar/Bot Telegram/temp/vidgif.mp4','rb')
    bot.send_video(chatid, vidgif)

    bot.send_message(chatid, "Intenta!")

    fry=open('/Users/fncg6/OneDrive/Escritorio/pruebas programar/Bot Telegram/temp/fry.mp4','rb')
    bot.send_video(chatid, fry)

    bot.send_message(chatid, "Y eso es todo, bienvenido oficialmente a Telegram")

@bot.message_handler(commands=['foto'])
def send_photo(message):
    chatid=message.chat.id
        
    bot.send_message(chatid, "wolas ")
    foto=open('/hola.png','rb')
    bot.send_photo(chatid, foto)

print("Ejecutandose")
bot.polling()
