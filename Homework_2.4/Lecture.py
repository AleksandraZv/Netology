# 1 part
#
# open('../menu.txt')

# 2 part

# import os
#
# print(os.getcwd())

# part 3 —

# import os
#
# print(os.getcwd())
# os.chdir('Переходим к nested')
# os.chdir('nested')
# print(os.getcwd())
# os.chdir('Переходим в /tmp')
# os.chdir('/tmp')
# print(os.getcwd())

# part 4 — пример использования os.path.join. Просто соединияет пути, но не проверяет их наличие. Не принимает списки.
# Только элементы

# import os
#
# p = os.path.join ('nested', 'nested2')
#
# p = os.path.join(*['nested', 'nested2']) # — args, конструкция валидна, запомнить как рабочий вариант
# print(p)

# part 5 — dirname

# import os
#
# print(os.path.dirname('/tmp/script.py'))
# print(os.path.dirname('/tmp/nested'))
# print(os.path.dirname('/tmp/nested/'))

# part 6 — примеры
import os
#
# print(os.path.abspath(os.path.dirname(__file__))) # — файл помогает где лежит переменная на самом деле

# print(__name__) # == '__main__'
#
# A = 100
#
# if __name__ == '__main__':
#     print('Главная программа!')
#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.abspath('else_dir'))

print(os.path.excist('bla-bla')) # — пример использования экзист
print(os.path.excist('book1'))