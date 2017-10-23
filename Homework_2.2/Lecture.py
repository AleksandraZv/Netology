# 1 part — пример обозначения ко

# # -*- coding: cp1251 =*=
# s = 'Hello, мир'
# print (s)

# 2 part

# s = 'Hello, мир'
#
# data = s.encode('cp1251')
# print(data)

# 3 part — узнать код у конкретного символа

# for c in range(ord('a'), ord('z')+1):
#     print(chr(c))

# 4 part — чтение файла с другой кодировкой

# with open('book1.txt', encoding='utf-8') as f:
#     data = f.read()
#     print(data[:50])

# 5 part — запись в файл с кодировкой

# with open('filename.txt', 'w', encoding='utf-8') as f:
#     s = 'Hello, мир'
#     f.write(s)

# 6 part

# import chardet
#
# with open('book1.txt', 'rb') as f:
#     data = f.read()
#     result = chardet.detect(data)
#     print(result)
#     # Выведет {'ancoding': 'windows-1251', 'confidence': 0.99, ..}
#     s = data.decode(result['encoding'])
