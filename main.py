from telethon.sync import TelegramClient, events
import os
from Ayarlar import *
from rich import print
from rich.console import Console
konsol = Console()

konsol.print("""[bold]---------------------------------- Program Başlatıldı | İndirme Başladı---------------------------------------------------------
t.me/kadirilgin1453 Herhangi Bir Sorunuz Yada Sorununuz Varsa Telegramdan Ulaşabilirsiniz.[/]""")

api_id = TG_APIID
api_hash = TG_APIHash

dosyakontrolFonksiyonu(api_hash,api_hash)

with TelegramClient('session.session', TG_APIID, TG_APIHash) as client:
    messages = client.iter_messages(TG_KanalAdi)
    os.mkdir(TG_KanalAdi)
    os.chdir(TG_KanalAdi) 
    for msg in messages:
        icerik = msg.media
        if Resim == "Evet":
            if "MessageMediaPhoto" in str(icerik):
                resimindir(msg)
        if Video == "Evet":
            if "video/mp4" in str(icerik):
                videoindir(msg)
        if Pdf == "Evet":
            if "application/pdf" in str(icerik):
                pdfindir(msg)
        if DigerDosyalar == "Evet":
            if "application/rar" in str(icerik):
                dosyaindir(msg)
            if "application/zip" in str(icerik):
                dosyaindir(msg)
            if "application/vnd.android.package-archive" in str(icerik):
                dosyaindir(msg)
