#Завдання 7. Використання методу Монте-Карло
#Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
#Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
#На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

import random
from collections import Counter

import matplotlib.pyplot as plt

N = 1_000_000


def simulate(n):
    counts = Counter(random.randint(1, 6) + random.randint(1, 6) for _ in range(n))
    return {s: counts[s] / n for s in range(2, 13)}


def analytical():
    return {s: (6 - abs(s - 7)) / 36 for s in range(2, 13)}


def print_table(mc, an):
    print(f"{'Сума':<6}{'Монте-Карло':>13}{'Аналітично':>13}{'Різниця':>10}")
    for s in range(2, 13):
        diff = abs(mc[s] - an[s])
        print(f"{s:<6}{mc[s]:>12.2%}{an[s]:>13.2%}{diff:>10.2%}")


def plot(mc, an):
    sums = list(range(2, 13))
    width = 0.4
    plt.bar([s - width / 2 for s in sums], [mc[s] * 100 for s in sums],
            width, label="Монте-Карло")
    plt.bar([s + width / 2 for s in sums], [an[s] * 100 for s in sums],
            width, label="Аналітично")
    plt.xticks(sums)
    plt.xlabel("Сума")
    plt.ylabel("Імовірність, %")
    plt.title(f"Кидки двох кубиків ({N:,} симуляцій)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    mc = simulate(N)
    an = analytical()
    print_table(mc, an)
    plot(mc, an)