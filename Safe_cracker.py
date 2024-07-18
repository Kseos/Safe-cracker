# This Python file uses the following encoding: utf-8
from random import randint, choice
import time


def fitness(combo, attempt):
    # Функция сравнивает элементы в двух списках и подсчитывает число совпадений
    match: int = 0
    for i, j in zip(combo, attempt):
        if i == j:
            match += 1
    return match


def main():
    # Создание переменной для комбинации, вывод на экран и конвертация в список
    combination = '4527571098'
    print('Комбинация = {}'.format(combination))
    combo = [int(i) for i in combination]

    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0
    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while best_attempt != combo:
        next_try = best_attempt[:]

        # Переменная lock_wheel - номер индекса, число под которым изменяется.
        # После сопадения индекс больше не используется. 
        lock_wheel = choice(indexes)
        next_try[lock_wheel] = randint(0, 9)
        next_try_grade = fitness(combo, next_try)

        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
            indexes.remove(lock_wheel)
            print(f"Число с индексом {lock_wheel + 1} верно!")

        print(next_try, best_attempt)
        count += 1

    print("\nВзломано! {}".format(best_attempt), end=' ')
    print("за {} попыток!".format(count))


start_time = time.time()
main()
end_time = time.time()
duration = end_time - start_time
print("Время выполнения этой программы составило {:.7f} секунд.".format(duration))
