from telegram.ext import Updater, CommandHandler
from functools import wraps


# ---------------------------------------------------------------------------------------------------------

# *********************************************************************************************************
# ********** UPDATER UTILITZANT EL TOKEN ******************************************************************
# *********************************************************************************************************

updater = Updater(token = '622284188:AAHn_kJkbU90RrRr8_vvx1DEJ3s8zt7YPM0')
dispatcher = updater.dispatcher

# ---------------------------------------------------------------------------------------------------------

# def send_typing_action(func):
#     """Sends typing action while processing func command."""

#     @wraps(func)
#     def command_func(*args, **kwargs):
#         bot, update = args
#         bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
#         func(bot, update, **kwargs)

#     return command_func

# ---------------------------------------------------------------------------------------------------------

# *********************************************************************************************************
# ********** ACCIONS BÀSIQUES *****************************************************************************
# *********************************************************************************************************

def help(bot, update):
	missatge = "Puc fer el següent:" + "\n\t- Presentar-me --> /nom" + "\n\t- Saludar --> /saluda <nom>"
	bot.send_message(chat_id = update.message.chat_id, text = missatge)


# @send_typing_action
def saluda_nom(bot, update, args):
    missatge = 'Hola ' + args[0] + '. Com estàs?'
    bot.send_message(chat_id = update.message.chat_id, text = missatge)

# @send_typing_action
def nom(bot, update):
    missatge = "Sóc l'ArrainoaBot. Què necessites?"
    bot.send_message(chat_id = update.message.chat_id, text = missatge)   

# ---------------------------------------------------------------------------------------------------------

# *********************************************************************************************************
# ********** CONNECTAR-SE A APIs **************************************************************************
# *********************************************************************************************************

#from divises import obtenir_equivalencia

#def conversio(bot, update, args):
#    missatge = obtenir_equivalencia(args[0], args[1], args[2])
#    bot.send_message(chat_id=update.message.chat_id, text=missatge)

# ---------------------------------------------------------------------------------------------------------

# *********************************************************************************************************
# ********** CRIDA DE LES FUNCIONS ************************************************************************
# *********************************************************************************************************

# BÀSIQUES:

help_handler = CommandHandler('help', help)
saluda_nom_handler = CommandHandler('saluda', saluda_nom, pass_args = True)
nom_handler = CommandHandler('nom', nom)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(saluda_nom_handler)
dispatcher.add_handler(nom_handler)

# APIs:

conversio_handler = CommandHandler('conversio', conversio, pass_args=True)

dispatcher.add_handler(conversio_handler)

updater.start_polling()
