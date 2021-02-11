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
artists = album_info[0]['artists']
artist = str(artists[0]['name'])
print('Artist: ', artist)
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
response = requests.get(f"https://api.discogs.com/database/search?q={artist}&key={secret.consumer_key}&secret={secret.consumer_secret}", headers=headers).content
response = str(response)
releases = d.search(album, artist=artist, type='release')
genres = []
styles = []
year = 0
labels = set([])
for i in releases:
    title = i.title.split("- ")[1]
    while title[0] == ' ':
        title = title[1:]
    while title[-1] == ' ':
        title = title[:-1]
    # print(i.title)
    # print(title, len(title), title.count(' '))
    # print(album, len(album), album.count(' '))
    if title == album:
        genres = i.genres
        styles = i.styles
        year = i.year
        labels = i.labels
        labels = i.data["label"]
        #print(i.data)
        print("Year: ", year)
        print("Genres: ", ', '.join(genres))
        print("Styles: ", ', '.join(styles))
        print("Labels: ", ', '.join(labels))
        break




# from yandex_music.client import Client
# import requests
# import discogs_client as discogs
# import secret
# import urllib.request
# from bs4 import BeautifulSoup
# import json
# import re
# #ЗАПРОС К ЯНДЕКС МУЗЫКЕ
# client = Client.from_credentials(secret.email, secret.password)
# album_string = input("Enter album url: ")
# #album_string = "https://music.yandex.ru/album/3837950"
# album_id_yandex = album_string.split('/')[-1]
# album_id_yandex = int(album_id_yandex)
# album_info = client.albums(album_id_yandex)
# album = str(album_info[0]['title'])
# album_arr = album.split()
# album = ''
# for i in album_arr:
#     album += i.capitalize()
#     album += ' '
# album = album[:-1]
# artists = album_info[0]['artists']
# artist = str(artists[0]['name'])
# print('Artist: ', artist)
# print('Album: ', album)
# # for artist in artists:
# #     print('Artist: ', artist['name']) //если артистов несколько
# # artist = client.artists(1401151)
# # print(artist[0]['name']) //выводится имя по id исполнителя
#
# #/database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}
# #ЗАПРОС К DISCOGS
# headers = {
#     'User-Agent': 'I',
#     'From': 'nerhneiro@gmail.com'
# }
# d = discogs.Client('musicSort/0.1', user_token=secret.user_token)
# response = requests.get(f"https://api.discogs.com/database/search?q={artist}&key={secret.consumer_key}&secret={secret.consumer_secret}", headers=headers).content
# response = str(response)
# releases = d.search(artist, type='artist')[0].releases
# album_id_discogs = -1
# for r in releases:
#     if r.data['type'] == "master" and r.data["role"] == "Main":
#         #print(r.data['title']) #вывод всех релизов исполнителя
#         print(".", end="")
#     if r.title == album:
#         album_id_discogs = r.id
#         break
# if album_id_discogs != -1:
#     try:
#         master_release = d.master(album_id_discogs)
#         print()
#         print(master_release.data)
#         master_release_data = master_release.data
#         album_styles = master_release.styles
#         album_year = int(master_release_data['year'])
#         album_genres = master_release_data['genres']
#         styles_type = str(type(album_styles)).split("'")[1].split("'")[0]
#         genres_type = str(type(album_genres)).split("'")[1].split("'")[0]
#         if genres_type != 'NoneType':
#             album_genres_string = ', '.join(album_genres)
#         else:
#             album_genres_string = "No information"
#         if styles_type != "NoneType":
#             album_styles_string = ', '.join(album_styles)
#         else:
#             album_styles_string = "No information"
#         print("Year: ", album_year)
#         print('Genres: ', album_genres_string)
#         print('Styles: ', album_styles_string)
#         labels = set([])
#         for i in master_release.versions:
#             release_id = i.id
#             release = d.release(release_id)
#             release_labels = release.labels
#             for j in release_labels:
#                 print(".", end="")
#                 release_label = str(j).split("'")[1]
#                 labels.add(release_label)
#         print()
#         print("Labels: ", ', '.join(labels))
#     except:
#         master_release = d.master(album_id_discogs)
#         data_id = master_release.data['id']
#         release = d.release(data_id)
#         print("Year: ", release.year)
#         if len(release.styles) == 0:
#             print("Genres: No information")
#         else:
#             print("Genres: ", ', '.join(release.genres))
#         if len(release.styles) == 0:
#             print("Styles: No information")
#         else:
#             print("Styles: ", ', '.join(release.styles))
#         labels = set([])
#         release_labels = release.labels
#         for j in release_labels:
#             release_label = str(j).split("'")[1]
#             labels.add(release_label)
#         if len(labels) == 0:
#             print("Labels: No information")
#         else:
#             print("Labels: ", ', '.join(labels))
