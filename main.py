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
        if Resim == "Evet" and "MessageMediaPhoto" in str(icerik):
            resimindir(msg)
            konsol.log("[bold] ✅ Resim İndirildi.[/]")
        if Video == "Evet" and "video/mp4" in str(icerik):
            videoindir(msg)
            konsol.log("[bold] ✅ Video İndirildi.[/]")
        if Pdf == "Evet" and "application/pdf" in str(icerik):
            pdfindir(msg)
            konsol.log("[bold] ✅ Pdf İndirildi.[/]")
        if DigerDosyalar == "Evet":
            if "application/rar" in str(icerik):
                dosyaindir(msg)
                konsol.log("[bold] ✅ Dosya İndirildi.[/]")
            if "application/zip" in str(icerik):
                dosyaindir(msg)
                konsol.print("[bold] ✅ Dosya İndirildi.[/]")
            if "application/vnd.android.package-archive" in str(icerik):
                dosyaindir(msg)
                konsol.log("[bold] ✅ 9Dosya İndirildi.[/]")
