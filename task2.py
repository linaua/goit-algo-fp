#Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
#Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

import math
import turtle


def pythagoras_tree(t, size, level):
    if level == 0:
        return

    pos = t.position()
    angle = t.heading()

    for _ in range(4):
        t.forward(size)
        t.left(90)

    t.left(90)
    t.forward(size)
    t.right(90)

    new_size = size * math.sqrt(2) / 2

    t.left(45)
    pythagoras_tree(t, new_size, level - 1)

    t.forward(new_size)
    t.right(90)
    pythagoras_tree(t, new_size, level - 1)

    t.penup()
    t.goto(pos)
    t.setheading(angle)
    t.pendown()


def main():
    level = int(input("Введіть рівень рекурсії (1-12): "))
    level = max(1, min(level, 12))

    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.tracer(0)  

    t = turtle.Turtle()
    t.hideturtle()

    size = 100
    t.penup()
    t.goto(-size / 2, -250)
    t.setheading(0)
    t.pendown()

    pythagoras_tree(t, size, level)

    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()