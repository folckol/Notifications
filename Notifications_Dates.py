import datetime
import time

import gspread
from pyrogram import Client

gs = gspread.service_account(filename='FILE.json')
ah = gs.open_by_key('')

worksheet = ah.worksheet('Под работу БОТА')
worksheet1 = ah.worksheet('ЗАДАЧИ')

start = 0

app = Client('Notification_session',
             api_id=,
             api_hash='')

used2 = []


used = []
used_1 = []
while True:

    value = worksheet.get_all_values()
    for deadline in value:

        deadline_data = deadline[5]

        message = ''

        if deadline_data.count('.') == 2:

            message+=f'Проект "{deadline[1]}"\n'

            date_now_day = datetime.datetime.now().day
            date_now_month = datetime.datetime.now().month
            date_now_year = datetime.datetime.now().year

            print(date_now_month)

            date_now = datetime.datetime(int(date_now_year), int(date_now_month), int(date_now_day))

            date_sheet_day = deadline_data.split(' ')[0].split('.')[0]
            date_sheet_month = deadline_data.split(' ')[0].split('.')[1]
            date_sheet_year = deadline_data.split(' ')[0].split('.')[2]

            date_sheet = datetime.datetime(int(date_sheet_year), int(date_sheet_month), int(date_sheet_day))

            try:
                change = str(date_sheet-date_now)
                print(change)



                if change.split(' ')[0] == '1':

                    if [deadline[0], 1] not in used:

                        used.append([deadline[0], 1])

                        with app:
                            app.send_message(-, f'До завершения события <i>{deadline[1]}</i> остался 1 день')

                if change.split(' ')[0] == '0:00:00':

                    if [deadline[0], 0] not in used:
                        used.append([deadline[0], 0])

                        with app:
                            app.send_message(-, f'Событие <i>{deadline[1]}</i> завершится сегодня, проверьте все данные и будьте готовы')

            except Exception as e:
                print(e)
                pass


    for deadline in value:

        deadline_data = deadline[6]

        message = ''

        if deadline_data.count('.') == 2:

            message+=f'Проект "{deadline[1]}"\n'

            date_now_day = datetime.datetime.now().day
            date_now_month = datetime.datetime.now().month
            date_now_year = datetime.datetime.now().year

            print(date_now_month)

            date_now = datetime.datetime(int(date_now_year), int(date_now_month), int(date_now_day))

            date_sheet_day = deadline_data.split(' ')[0].split('.')[0]
            date_sheet_month = deadline_data.split(' ')[0].split('.')[1]
            date_sheet_year = deadline_data.split(' ')[0].split('.')[2]

            date_sheet = datetime.datetime(int(date_sheet_year), int(date_sheet_month), int(date_sheet_day))

            try:
                change = str(date_sheet-date_now)
                print(change)



                if change.split(' ')[0] == '1':

                    if [deadline[0], 1] not in used_1:

                        used_1.append([deadline[0], 1])

                        with app:
                            app.send_message(-, f'До минта в событии <i>{deadline[1]}</i> остался 1 день')

                if change.split(' ')[0] == '0:00:00':

                    if [deadline[0], 0] not in used_1:
                        used_1.append([deadline[0], 0])

                        with app:
                            app.send_message(-, f'Минт <i>{deadline[1]}</i> уже сегодня, будьте готовы')

            except Exception as e:
                print(e)
                pass


    notes = worksheet1.get_all_values()
    count = 1
    for deadline in notes:

        if deadline[1] == '':
            continue

        if start == 0:
            used2.append([deadline[0], deadline[1], deadline[2], deadline[3]])
            count+=1

            if count == 15:

                start = 1

            continue

        print([deadline[0], deadline[1], deadline[2], deadline[3]])
        print(used2)
        if [deadline[0], deadline[1], deadline[2], deadline[3]] not in used2 and (deadline[0] != '' and deadline[1] != '' and deadline[2] != '' and deadline[3] != ''):
            print(111)

            used2.append([deadline[0], deadline[1], deadline[2], deadline[3]])

            with app:


                nick = ''
                if deadline[0] == 'DD':
                    nick = '@DD'
                #

                app.send_message(-, f'Для {nick} появилась новая задача.\n\n'
                                                 f'Проект: {deadline[1]}\n'
                                                 f'Суть: {deadline[2]}\n'
                                                 f'Дедлайн: {deadline[3]}')

        count += 1

    print(used2)
    print('\n\n')



    time.sleep(100)






