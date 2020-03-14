#!/usr/bin/env python3
import json
import os
import requests
from bs4 import BeautifulSoup
import time
import random

def crawl_youtube_id(singer, song_name):
    url = "https://www.youtube.com/results?search_query=" + singer + "+" + song_name
    print(url)
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    meow = soup.select_one(".yt-lockup-video")
    count = 0
    while not meow:
        if count == 10:
            return "/watch?v=rSJ4jtghTDc"
#		time.sleep(random.random() * 10)
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        meow = soup.select_one(".yt-lockup-video")
        count += 1
    data = meow.select("a[rel='spf-prefetch']")
    if data == []:
        return "/watch?v=ctfEmKL8beE"
    return data[0].get("href")


def main():
    fn = input("songs.json: ")
    cnt = 0
    songs = []
    with open(fn, "r") as fp:
        songs = json.load(fp)
    print("loaded.")
    idx = 0
    for song in songs:
        idx += 1
        if idx % 100 == 0:
            print(idx)
        if song['youtube_id'] != '/watch?v=rSJ4jtghTDc':
            continue
        print(idx - 1, song['date'][:4], song['name'], song['youtube_id'])
        tot = 0
        song['youtube_id'] = crawl_youtube_id(song['singer'], song['name'])
        while song['youtube_id'][:9] != '/watch?v=':
            song['youtube_id'] = crawl_youtube_id(song['singer'], song['name'])
            tot += 1
            if tot == 10:
                song['youtube_id'] = '/watch?v=ctfEmKL8beE'
        print(song['youtube_id'])
        cnt += 1
        if cnt % 100 == 0:
            with open(fn, "w") as fp:
                json.dump(songs, fp)
            print("saved")
    with open(fn, "w") as fp:
        json.dump(songs, fp)
    print("saved")


if __name__ == '__main__':
    walk()
