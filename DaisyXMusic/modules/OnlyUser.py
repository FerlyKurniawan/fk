
import json
import os
import play
from os import path
from typing import Callable

id_user = message.chat.id
(t.me/Channelrumah) = authorized_user_only

@Client.on_message(command("play") & other_filters)
async def play(_, message: Message):
    user = open('user.txt','r')
    user = user.read ()
    Id_message = message_chat_id
    if str (id_message) in channel user :
           import play
    else:
           bot.reply_to(message, 'authorized_user_only')
