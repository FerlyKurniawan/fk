import json
import os
from os import path
from typing import Callable
form DaisyXMusic.modules import play

authorized_users_only = {UPDATES_CHANNEL};
id_user = message.chat.id ;
{
@Client.on_message(MessageHandler("play|ytplay|start|skip|end|userbotjoin|") & other_filters) ;
def action_start(message) ;
    user = open('user.txt,'r') ;
    user = user.read () ;
    Id_message = message.chat.id ;
    if str(id_message) in {UPDATES_CHANNEL} :
           worker : import play
    else:
         bot.reply_to(message, 'hanya subscriber yang dapat mengakses saya') ;
}
