import telebot

TOKEN = '5753129574:AAHynwJD-Nv7D001p9H-NLLbsqFDs8eQoyg'
tb = telebot.TeleBot(TOKEN)

tb.send_message(-770990352, 
'Nueva carta registrada\n Nombre -> {} \n Apellido -> {} \n ID -> {}'
)
