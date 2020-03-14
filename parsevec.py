#/usr/bin/env python3
import json

vector = open(input("docvectors.txt: "), "r")

f = open(input("Log file: "), "r")
songs = []

for i in f.readlines():
    path = i.strip()
	with open(path, 'r') as fp:
		print(path)
		song_list = json.load(fp)
		for song in song_list :
			getvec = vector.readline().strip()
			song['vecvalue'] = list(map(float, getvec.split(' ')))
            songs.append(song)
	
	print(f"Finish {path} !")
vector.close()
f.close()

with open("data/songs.json", "w") as fp:
    json.dump(songs, fp)

for song in songs:
    del song['vecvalue']
with open("web/songs.json", "w") as fp:
    json.dump(songs, fp)
