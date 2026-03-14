import telebot
import random
TOKEN = "8533991093:AAGHXv6DLsp2reTyVkcAttKowh0dde7uyW0"
bot = telebot.TeleBot(TOKEN)

questions = [
    ("Почему космические ракеты не могут передвигаться внутри Солнечной системы по кратчайшим путям", "потому что их пути искривляются под действием притяжения Солнца, Земли, Луны и других небесных тел"),
    ("Какая планета Солнечной системы имеет самое большое количество спутников?", "Сатурн он имеет 62 естественных спутника"),
    ("С помощью какой звезды находят стороны света?", "Полярная звезда"),
    ("Как называются очень маленькие и очень плотные звёзды, которые представляют собой конечную стадию эволюции звёзд?", "Белые карлики")
]

scores = {}
current = {}

@bot.message_handler(commands=['start'])
def start(message):

    scores[message.chat.id] = 0

    bot.send_message(message.chat.id,
                     "Напишите /next")
    
@bot.message_handler(commands=['next'])
def next_question(message):

    q = random.choice(questions)
    current[message.chat.id] = q

    bot.send_message(message.chat.id,
                     q[0])
    
@bot.message_handler(func=lambda message: True)
def answer(message):

    q = current.get(message.chat.id)

    if not q:
        return
    
    if message.text.lower() == q[1]:
        scores[message.chat.id] += 1
        bot.send_message(message.chat.id,
                         "Верно")
        
    else:
        bot.send_message(message.chat.id,
                         f"Ответ: {q[1]}")

bot.infinity_polling()