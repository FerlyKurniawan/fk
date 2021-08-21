
import json
import os
import play
from os import path
from typing import Callable

id_user = message.chat.id

@bot.message_handler(commands=['play'])
def action_start(message)
    user = open('user.txt','r')
    user = user.read ()
    Id_message = message_chat_id
    if str (id_message) in channel user :
           import play
    else:
           bot.reply_to(message, 'authorized_users_only')
