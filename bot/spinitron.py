#!/usr/bin/env python3

import datetime

from bs4 import BeautifulSoup
import requests

TEST_PAGE = "/home/jerry/Documents/kxlu_spinitron.html"
KXLU_PAGE = "https://spinitron.com/KXLU/"


response = requests.get(KXLU_PAGE)
t = response.text
# t = open(TEST_PAGE).read()

soup = BeautifulSoup(t, "html.parser")

show_title = None
dj_name = None
artist = "Unknown"
song = ""
fh = open("last_song.txt", "r")
last_song = fh.read()
fh.close()

for h3 in soup.find_all("h3"):
    myclass = h3.get("class")
    if myclass == ["show-title"]:
        show_title = h3.a.text

for p in soup.find_all("p"):
    myclass = p.get("class")
    if myclass == ["dj-name"]:
        dj_name = p.a.text

for div in soup.find_all("div"):
    myclass = div.get("class")
    if myclass == ["spin"]:
        artist = div.span.text
        break

for span in soup.find_all("span"):
    myclass = span.get("class")
    if myclass == ["song"]:
        song = span.text
        break

if last_song != song:
    last_song = song
    fh = open("last_song.txt", "w")
    fh.write(song)
    fh.close()
    fh = open("chat.log", "a")
    fh.write("\n%s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    fh.write(f"Now playing: {song} - {artist}\n\n")
    fh.close()
    print(f"{song} - {artist}\n")

    fh = open("playlist.txt", "a")
    fh.write(f"{song} - {artist}\n")
    fh.close()

if show_title and dj_name:
    # print(f"You are listenging to {show_title} with {dj_name}.")
    print(f"{artist} - {song}")
# else:
#    print("The current show is unknown (Spinitron has not been updated.)")

# for link in soup.find_all("a"):
#    href = link.get("href")
#    print(href)
