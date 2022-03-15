from telethon import TelegramClient, events, sync
from json import load
import os
MainConfig = load((open('config.json', 'r+', encoding='utf8')))
TG_APIID    = MainConfig['TG_APIID']
TG_APIHash  = MainConfig['TG_APIHash']
TG_KanalAdi    = MainConfig['TG_KanalAdi']
Video = MainConfig['Video']
Pdf = MainConfig['Pdf']
Resim = MainConfig['Resim']
DigerDosyalar = MainConfig['DigerDosyalar']
#Session Kontrolü
def dosyakontrolFonksiyonu(api_id,api_hash):
    dosyakontrol = os.path.isfile("session.session")
    if dosyakontrol == False:
        client = TelegramClient("session.session", api_id, api_hash)
        client.start()
        client.disconnect()
# Kanal Yada Gruptaki Resmi İndirme Fonksiyonu
def resimindir(msg):
    filename = 'resim'
    msg.download_media(file=os.path.join('resimler', filename))
# Kanal Yada Gruptaki Videoyu İndirme Fonksiyonu
def videoindir(msg):
    filename = 'video'
    msg.download_media(file=os.path.join('videolar', filename))
# Kanal Yada Gruptaki Pdf'i İndirme Fonksiyonu
def pdfindir(msg):
    filename = msg.file.name
    msg.download_media(file=os.path.join('pdlfer', filename))
# Kanal Yada Gruptaki Dosyalar'ı İndirme Fonksiyonu
def dosyaindir(msg):
    filename = msg.file.name
    msg.download_media(file=os.path.join('dosyalar', str(filename)))