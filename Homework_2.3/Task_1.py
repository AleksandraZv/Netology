import json
import chardet
import os
from collections import Counter, defaultdict


def get_ten_popular_words(data):
    news_list = data['rss']['channel']['items']
    words = []
    for news in news_list:
        words.extend(news['description'].split(' '))
    freqword = defaultdict(list)
    for word, freq in Counter(words).items():
        if len(word) > 6:
            freqword[freq].append(word)

    for freq in sorted(freqword, reverse=True)[:10]:
        print('count {}: {}'.format(freq, sorted(freqword[freq])))


def get_data():
    with open('newsafr.json', 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        data = json.load(file)
        return data


def analyze_news():

    for file in os.listdir("./"):
        if file.endswith(".json"):
            print('10 most usable words with length > 6 in file ', file, ':')
            data = get_data(file)
            get_ten_popular_words(data)
            print('-----------------------------------------------------')


analyze_news()