# Copyright (c) 2016-2017 The OrarioTreniBot Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json

import config
from ..objects.user import User


def process_start_command(bot, message):
    u = User(message.sender)
    u.state("home")
    u.increaseStat('stats_command_start')

    text = (
        "<b>Benvenuto in Orario Treni Bot!</b>"
        "\nCon questo bot potrai cercare 🚅 <b>treni</b>, 🚉 <b>stazioni</b> e 🚊 <b>itinerari</b> "
        "anche ☑️ <b>inline</b>!"
        "\nPremi uno dei <b>tasti qui sotto</b> per iniziare"
    )
    bot.api.call('sendMessage', {
        'chat_id': message.chat.id, 'text': text, 'parse_mode': 'HTML', 'reply_markup':
        json.dumps(
            {'inline_keyboard': [
                [{"text": "🚅 Cerca treno", "callback_data": "train"},
                 {"text": "🚉 Cerca stazione", "callback_data": "station"}],
                [{"text": "📰 News", "callback_data": "news"},
                 {"text": "🛤 Treni in tracciamento", "callback_data": "tracks"}],
                [{"text": "ℹ️ Altre informazioni", "callback_data": "info"}]
            ]}
        )
    })


def process_admin_command(bot, message):
    if message.sender.id not in config.ADMINS:
        return

    text = (
        "🔴 <b>Benvenuto nel pannello amministratore di Orario Treni</b>"
        "\nSeleziona un opzione:"
    )
    bot.api.call('sendMessage', {
        'chat_id': message.chat.id, 'text': text, 'parse_mode': 'HTML', 'reply_markup':
        json.dumps(
            {'inline_keyboard': [
                [{"text": "➕🌐 Nuovo post globale", "callback_data": "admin@newpost"}]
            ]}
        )
    })
