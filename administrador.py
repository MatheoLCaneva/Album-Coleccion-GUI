import telebot

def mandarMensaje(a, b, c):
    TOKEN = '5753129574:AAHynwJD-Nv7D001p9H-NLLbsqFDs8eQoyg'
    tb = telebot.TeleBot(TOKEN)
    tb.send_message(-770990352, '-------------------------------------------\nNueva carta registrada\n Nombre -> {} \n Apellido -> {} \n ID -> {}\n-------------------------------------------'.format(a,b,c))
    print('a')




