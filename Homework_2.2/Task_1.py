import chardet
import operator

def define_encoding(filename):

    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        return result

def get_data(filename, enc):

    with open(filename, encoding=enc['encoding']) as f:
        data = f.read().lower()
        #print(data)

        words = data.split(' ')
        #print(words)

        word_dict = {}
        for word in words:
            if len(word) > 6:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

        #print(word_dict)

        sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

        #print(sorted_word_dict)

        print(sorted_word_dict[:10])

filename = 'newsfr.txt'
enc = define_encoding(filename)
get_data(filename, enc)

filename = 'newsit.txt'
enc = define_encoding(filename)
get_data(filename, enc)

filename = 'newsafr.txt'
enc = define_encoding(filename)
get_data(filename, enc)

filename = 'newscy.txt'
enc = define_encoding(filename)
get_data(filename, enc)