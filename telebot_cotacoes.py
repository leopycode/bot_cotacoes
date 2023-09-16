import telebot
import requests
from time import sleep

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,ARS-BRL,CLP-BRL,GBP-BRL")
cotacao = cotacao.json()
cot_dolar = cotacao["USDBRL"]["bid"]
cot_euro = cotacao["EURBRL"]["bid"]
cot_libra = cotacao["GBPBRL"]["bid"]

chave_api = "5982925804:AAHLrfP6nZxKznj9UMm6uEyl5YtIMryfem4"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=["Dolar"])
def dolar(mensagem):
    dolar = float(cot_dolar)
    bot.send_message(mensagem.chat. id, f"A cotação atual do Dolar é de R$ {dolar:.2f}")
    sleep(2)
    bot.send_message(mensagem.chat.id, "Obrigado por sua interação. Volte sempre.")

@bot.message_handler(commands=["Euro"])
def euro(mensagem):
    euro = float(cot_euro)
    bot.send_message(mensagem.chat. id, f"A cotação atual do Euro é de R$ {euro:.2f}")
    sleep(2)
    bot.send_message(mensagem.chat.id, "Obrigado por sua interação. Volte sempre")

@bot.message_handler(commands=["Libra_Esterlina"])
def libra(mensagem):
    libra = float(cot_libra)
    bot.send_message(mensagem.chat. id, f"A cotação atual da Libra Esterlina é de R$ {libra:.2f}")
    sleep(2)
    bot.send_message(mensagem.chat.id, "Obrigado por sua interação. Volte sempre")

@bot.message_handler(commands=["Nao_quero_de_consultar_agora"])
def nao(mensagem):
    bot.send_message(mensagem.chat. id, "Obrigado por sua interação. Volte sempre.")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Olá! Gostaria de consultar a cotação de qual moeda? \n   /Dolar \n   "
                                       "/Euro \n   /Libra_Esterlina \n   /Nao_quero_de_consultar_agora ")

bot.polling()
