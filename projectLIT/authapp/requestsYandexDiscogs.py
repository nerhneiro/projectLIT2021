from yandex_music.client import Client
import requests
import discogs_api as discogs
import authapp.secret as secret
from PIL import Image
import urllib.request
from bs4 import BeautifulSoup
import json
import re

def get_info(album, artists):
    headers = {
        'User-Agent': 'I',
        'From': 'nerhneiro@gmail.com'
    }
    print('Album:', album)
    print('Artists: ', *artists)
    d = discogs.Client('musicSort/0.1', user_token=secret.user_token)
    genres = []
    styles = []
    year = 0
    labels = set([])
    idDiscogs = 0
    searching = True
    for artist, idArtist in artists:
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
                    idDiscogs = i.id
                    genres = i.genres
                    styles = i.styles
                    year = i.year
                    # labels = i.labels
                    labelsNames = i.data["label"]
                    for l in labelsNames:
                        label = d.search(l, type='label')
                        labels.add((l, label[0].id))
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
                        print('Labels: ', end='')
                        for l, idLabel in labels:
                            print(l, end=', ')

                    except:
                        print("Labels: No information")
                    searching = False
                    break
        else:
            break
    print('\n')
    return year, genres, styles, labels, idDiscogs