from src.song import Song
from tinytag import TinyTag
import pathlib
import os
import re

location = 'f:/Music/'
target = 'f:/pyMusic/'
files_in_dir = []
songs = []


def getSong(item):
    tags = TinyTag.get(item)
    return Song(tags.title, item, rmPunct(tags.artist.split('/')[0]), rmPunct(tags.album))


def rmPunct(item):
    reg = re.compile('[^a-zA-ZА-Яа-я0-9_\- ]')
    return reg.sub('', item)


def printSong(song):
    print('=======')
    print(song.path)
    print("Title: " + song.title)
    print("Artist: " + song.author)
    print("Album: " + song.album)


def moveSong(song):
    artistDir = target + song.author
    albumDir = (target + song.author + '\\' + song.album).strip()
    newPath = albumDir + '\\' + os.path.basename(song.path)
    if (not os.path.exists(artistDir)):
        pathlib.Path(artistDir).mkdir(parents=True, exist_ok=True)
    if (not os.path.exists(albumDir)):
        pathlib.Path(albumDir).mkdir(parents=True, exist_ok=True)
    if (os.path.exists(newPath)):
        newPath = newPath + ".copy"
        print("COPY: " + newPath)
    os.replace(song.path, newPath)


def main():
    if (not os.path.exists(target)):
        pathlib.Path(target).mkdir(parents=True, exist_ok=True)

    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            files_in_dir.append(os.path.join(r, item))

    for item in files_in_dir:
        # print("file in dir: ", item)
        songs.append(getSong(item))

    for song in songs:
        # printSong(song)
        moveSong(song)


main();
