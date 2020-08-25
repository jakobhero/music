from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os

dir_contents=os.listdir()
mp3s=[]
for item in dir_contents:
    if item.split(".")[-1]=="mp3":
        mp3s.append(item)
for filename in mp3s:
    song=MP3File(filename)
    tags=song.get_tags()["ID3TagV2"]
    song.set_version(VERSION_BOTH)
    song.artist=tags["band"].lower()
    song.album=tags["album"].lower()
    song.song=tags["song"].lower()
    song.band=tags["band"].lower()
    song.comment=""
    song.save()
