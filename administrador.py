import telebot    
import csv

def mandarMensaje(a, b, c):
    TOKEN = '5753129574:AAHynwJD-Nv7D001p9H-NLLbsqFDs8eQoyg'
    tb = telebot.TeleBot(TOKEN)
    tb.send_message(-770990352, '-------------------------------------------\nNueva carta registrada\n Nombre -> {} \n Apellido -> {} \n ID -> {}\n-------------------------------------------'.format(a, b, c))
    print('a')


def almacenar(Nombre, Apellido, Codigo):
    obj = [Nombre, Apellido, Codigo]

    with open(r'C:\Users\Matheo\Desktop\testTk\Album-Coleccion-GUI/test.csv', "a", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(obj)


def buscar(Codigo):
    condicion = False
    with open(r'C:\Users\Matheo\Desktop\testTk\Album-Coleccion-GUI/test.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[2] == Codigo:
                condicion = True
    return condicion