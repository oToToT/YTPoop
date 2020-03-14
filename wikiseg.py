#!/usr/bin/env python3
from gensim.corpora import WikiCorpus
from ckiptagger import WS
from opencc import OpenCC

S_TO_TWP = OpenCC('s2twp').convert
ws = WS("./ckiptagger")

def getfile():
    try:
        r = input('wikidump.xml.bz2: ')
        open(r, 'r').close()
        return r
    except FileNotFoundError:
        print('File Not Found!')
        return None

def main():
    wiki = WikiCorpus(getfile())
    output = open(input('output: '), 'w', encoding='utf-8')
    texts_num = 0
    for text in wiki.get_texts():
        page = S_TO_TWP(' '.join(text))
        words = ws([page], segment_delimiter_set={",", "。", ":", "?", "!", ";", " "}, sentence_segmentation=True)
        for word in words:
            for char in word:
                if char != ' ':
                    output.write(char + ' ')
        output.write('\n')
        texts_num += 1
        if texts_num % 10000 == 0:
            print('已完成前 %d 行的斷詞' % texts_num)

if __name__ == '__main__':
    main()

