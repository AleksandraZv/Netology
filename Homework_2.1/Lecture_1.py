# Part_1 — первый пример с лекции

# f = open('hello.txt',encoding='utf-8')
# print(f.readline(), end='')
# print('---')
# print(f.readline(), end='')
# print('---')
# print(f.readline(), end='')
# f.close()

# Part_2 — второй пример с лекции

# with open('hello.txt') as f:
#     print(f.readline())
#
# f.readline()

# Part_3 — третий пример с лекции

# f = open('hello.txt', encoding='utf-8')
# for line in f:
#     print ('Следующая строка')
#     print(line)

# Part_4 — четвёртый пример с лекции

# count = 0
#
# with open('book1.txt', encoding='utf-8') as f:
#     for l in f:
#         lower_l = l.lower()
#         if 'пьер' in lower_l and 'наташа' in lower_l:
#             count += 1
#             print('Строка:')
#             print(l)
#
# print('Пьер и Наташа были вместе на {} строках'. format(count))

# Part_5 — пятый пример с лекции

max_avg = None
best_grade = None

with open('ratings.txt', encoding='utf-8') as f:
    for line in f:
        grade = line.strip()
        ratings = f.readline()
        ratings = ratings.strip()
        ratings_list = ratings.split()
        result_list = []
        for rating in ratings_list:
            result_list.append(int(rating))
        print(result_list)
# result_list = [int(rating) for rating in ratings_list] — вариант вместо трёх строк выше (лист компрехеншен)
# result_list = list(map(lambda x: int(x), ratings_list)) — ещё вариант (мап)
        avg_rating = sum(result_list) / len(result_list)
        if max_avg is None or avg_rating > max_avg:
            max_avg = avg_rating
            best_grade = grade

        print('Класс: {}, его оценки: {}'.format(grade, ratings))
        f.readline()

print('Класс с лучшей оценкой: {}. Его оценка: {}'.format(best_grade, max_avg))
