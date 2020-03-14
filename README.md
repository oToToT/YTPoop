# YTPoop #

## Intro ##

A song recommendation system with lyrics data.

- Member
  - [@minson123](https://github.com/minson123-github)
  - [@harry900831](https://github.com/harry900831)
  - [@oToToT](https://github.com/oToToT)
- Instructor: Pu-Jen Cheng

Slides: [https://dve.tw/V5B](https://dve.tw/V5B)

## HowTo ##

### Build up song database ###

You could use [@harry900831/mojim_lyrics_crawler](https://github.com/harry900831/mojim_lyrics_crawler) to crawl song data from [mojim.com](http://mojim.com/).

After that, you should use `load_lyrics.py` to segment lyrics. Notice that we use [ckiptagger](https://github.com/ckiplab/ckiptagger) to segment lyrics, you should download it to `./ckiptagger/`.

Then, we need to use [doc2vecC](https://github.com/mchen24/iclr2017) to perform doc2vec operation. However, we might want to add more corpus to train our data, so you could download [dump](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2) of wikipedia. To extract data from dumped data, you could use `wikiseg.py` to segment data.

Also, you might want to concat and shuffle wikicorpus and lyrics data.

Here is some notes to use doc2vecC (assuming corpus in `corpus.txt` and lyrics data in `lyrics.txt`):
1. `wget https://raw.githubusercontent.com/mchen24/iclr2017/master/doc2vecc.c`
2. `gcc doc2vecc.c -o doc2vecc -lm -pthread -O3 -march=native -funroll-loops`
3. `./doc2vecc -train corpus.txt -word wordvectors.txt -output docvectors.txt -cbow 1 -size 100 -window 10 -negative 5 -hs 0 -sample 0 -threads 4 -binary 0 -iter 20 -min-count 10 -test lyrics.txt -sentence-sample 0.1 -save-vocab alldata.vocab`

With docvectors generated, you might want to merge them back into the origin data, so you could run `parsevec.py` with log generated from `load_lyrics.py`. It will generate two `data/songs.json` without docvector inside it and `web/songs.json` with docvector inside it.

Then, you need to add youtube link to every songs, you could use `youtubeid.py` to brute-forced crawl youtube data.

p.s [KKBOX](https://www.kkbox.com/) has provided a great [API](https://github.com/KKBOX/OpenAPI-Python) for songs data, but we doesn't know that before.

### Launch Elasticsearch service ###

You could try to use Dockerfile inside `data` to launch a elsaticsearch sevice.

### Launch Web Server ###

You could try to use Dockerfile inside `web` to launch a server from [@oToToT/YTPoop-Server](https://github.com/oToToT/YTPoop-Server). Notice that you may want to change the path to sqlite database or try other database, and also you could change `session_secret` inside it.

