import datetime
import time

import gspread
from pyrogram import Client, types

start = 0

app = Client('Notification_session',
             api_id=,
             api_hash='')

@app.on_message()
def my_handler(client: Client, message: types.Message):

    # print(message.text)
    try:
        text = message.text.html

        text = text.replace('<b>', '**')
        text = text.replace('</b>', '**')

        text = text.replace('<i>', '*')
        text = text.replace('</i>', '*')

        text = text.replace('<s>', '~~')
        text = text.replace('</s>', '~~')

        text = text.replace('<u>', '**')
        text = text.replace('</u>', '**')

        text = text.replace('<code>', '*')
        text = text.replace('</code>', '*')

        text = text.replace('</a>', '')

        while text.count('<a href') != 0:
            # print(text.find('<a href="') + 9, )
            link = text[(text.find('<a href="') + 9):text[(text.find('<a href="') + 9):].find('>') + 8 + text.find('<a href="')]
            # print(link)
            text = text.replace(f'<a href="{link}">', f'({link}) ')
            time.sleep(1)


        print('\n\n\n', text)
    except:
        print(message.text)



app.run()



