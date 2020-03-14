#!/usr/bin/env python3
import os
import json
from ckiptagger import WS

d = input('Directory: ')
o = input('Output: ')
g = input('Log: ')

of = open(o, 'w')
gf = open(g, 'w')
songs_count = 0

ws = WS("./ckiptagger")

for path, dirs, files in os.walk(d):
    for f in files:
        if not f.endswith('.json'):
            continue
        fpath = os.path.join(path, f)
        gf.write(fpath + '\n')
        with open(fpath, 'r') as fp:
            songs = json.load(fp)
            for song in songs:
                lyrics = ' '.join(song['lyrics']).replace(r'　', ' ')
                of.write(lyrics)
                for word in ws([lyrics], segment_delimiter_set={",", "。", ":", "?", "!", ";", " "}, sentence_segmentation=True):
                    for char in word:
                        if char != ' ':
                            of.write(char + ' ')
                of.write('\n')
                songs_count += 1
                if songs_count % 1000 == 0:
                    print('已處理 %d 首歌' % songs_count)

of.close()
gf.close()

print('完成處理 %d 首歌' % songs_count)
