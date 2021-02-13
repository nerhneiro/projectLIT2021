from yandex_music.client import Client
import requests
import discogs_api as discogs
import secret

import urllib.request
from bs4 import BeautifulSoup
import json
import re
def get_info(album_string):
    client = Client.from_credentials(secret.email, secret.password)

    genres = []
    styles = []
    year = 0
    labels = set([])

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
    # ЗАПРОС К DISCOGS
    d = discogs.Client('musicSort/0.1', user_token=secret.user_token)
    searching = True
    for artist in artists:
        if searching:
            releases = d.search(album, artist=artist, type='release')
            # print("artist ", artist)
            for i in releases:
                title = i.title.split("- ")[1]
                while title[0] == ' ':
                    title = title[1:]
                while title[-1] == ' ':
                    title = title[:-1]
                # можно просто брать первый найденный релиз!
                # print(i.title)
                # print(title.upper(), len(title), title.count(' '))
                # print(album.upper(), len(album), album.count(' '))
                if title.upper() == album.upper():
                    genres = i.genres
                    styles = i.styles
                    year = i.year
                    # labels = i.labels
                    labels = i.data["label"]
                    for ar in i.data["artists"]:
                        print(ar["id"])
                    # print(i.data)
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
        return artists, album, year, genres, styles, labels
        #new_artist = Artist()
#ЗАПРОС К ЯНДЕКС МУЗЫКЕ

urls = ['https://music.yandex.ru/album/6979957', 'https://music.yandex.ru/album/605220', 'https://music.yandex.ru/album/67415']
#album_string = input("Enter album url: ")
#album_string = "https://music.yandex.ru/album/3837950"
for url in urls:
    artists, album, year, genres, styles, labels = get_info(url)
    print('________')

#get artist id discogs and labels id from discogs