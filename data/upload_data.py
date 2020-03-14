#!/usr/bin/env python3
import json
from elasticsearch import Elasticsearch

es = Elasticsearch()

with open('/ytp/songs.json', 'r') as fp:
    songs = json.load(fp)
    for i in range(len(songs)):
        es.index(index="songs", id=i, body=songs[i])
        if i % 1000 == 0:
            print(i, songs[i]['singer'], songs[i]['name'])
