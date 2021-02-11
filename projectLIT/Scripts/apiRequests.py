from yandex_music.client import Client
import requests
import discogs_api as discogs
import secret
import urllib.request
from bs4 import BeautifulSoup
import json
import re
#ЗАПРОС К ЯНДЕКС МУЗЫКЕ
client = Client.from_credentials(secret.email, secret.password)
album_string = input("Enter album url: ")
#album_string = "https://music.yandex.ru/album/3837950"
album_id_yandex = album_string.split('/')[-1]
album_id_yandex = int(album_id_yandex)
album_info = client.albums(album_id_yandex)
album = str(album_info[0]['title'])
album_arr = album.split()
album = ''
for i in album_arr:
    album += i.capitalize()
    album += ' '
album = album[:-1]
artistsAll = album_info[0]['artists']
artists = []
for i in artistsAll:
    artists.append(i["name"])
print('Artist(s): ', ', '.join(artists))
print('Album: ', album)
# for artist in artists:
#     print('Artist: ', artist['name']) //если артистов несколько
# artist = client.artists(1401151)
# print(artist[0]['name']) //выводится имя по id исполнителя

#/database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}
#ЗАПРОС К DISCOGS
headers = {
    'User-Agent': 'I',
    'From': 'nerhneiro@gmail.com'
}
d = discogs.Client('musicSort/0.1', user_token=secret.user_token)
# response = requests.get(f"https://api.discogs.com/database/search?q={artists[0]}&key={secret.consumer_key}&secret={secret.consumer_secret}", headers=headers).content
# response = str(response)

genres = []
styles = []
year = 0
labels = set([])

searching = True
for artist in artists:
    if searching == True:
        releases = d.search(album, artist=artist, type='release')
        for i in releases:
            title = i.title.split("- ")[1]
            while title[0] == ' ':
                title = title[1:]
            while title[-1] == ' ':
                title = title[:-1]
            # print(i.title)
            # print(title.upper(), len(title), title.count(' '))
            # print(album.upper(), len(album), album.count(' '))
            if title.upper() == album.upper():
                genres = i.genres
                styles = i.styles
                year = i.year
                labels = i.labels
                labels = i.data["label"]
                #print(i.data)
                print("Year: ", year)
                try:
                    print("Genres: ", ', '.join(genres))
                except:
                    print("Genres: No information")
                try:
                    print("Styles: ", ', '.join(styles))
                except:
                    print("Styles: No information")
                try:
                    print("Labels: ", ', '.join(labels))
                except:
                    print("Labels: No information")
                searching = False
                break
    else:
        break
