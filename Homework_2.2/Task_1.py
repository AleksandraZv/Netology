import chardet
import re
import string
frequency = {}

def define_encoding():

    with open('newscy.txt', 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)

def get_data():

    with open('newscy.txt', 'r', encoding='KOI8-R') as f:
        data = f.read().lower()
        if word in data: # как написать, что если в данных есть слово больше 6 букв? Это регулярные выражения?
            frequency_word = count + 1 # если есть значит считаем +1
            # дальше мы мы должны написать что-то вроде если count = 10, то перенести это в словарь?


        word_search = re.search(r'\b[а-я]{6-10}\b', data) # — этот вариант почему-то не работает
        for word in word_search:
            count = frequency.get(word,0)
            frequency[word] = count + 1

            frequency_list = frequency.keys()

            for words in frequency_list:
                print (words, frequency[words])

define_encoding()
get_data()

