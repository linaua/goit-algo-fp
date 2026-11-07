#Завдання 6. Жадібні алгоритми та динамічне програмування
#Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
#Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
#Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
#Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.


from matplotlib.pyplot import hot


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    ranked = sorted(items.items(),
                    key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
                    reverse=True)
    chosen, total_cost, total_calories = [], 0, 0
    for name, info in ranked:
        if total_cost + info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items)
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        cal = items[names[i - 1]]["calories"]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + cal)

    chosen, b = [], budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]
    chosen.reverse()

    total_cost = sum(items[name]["cost"] for name in chosen)
    return chosen, total_cost, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    g_items, g_cost, g_cal = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print(f"  страви: {g_items}, вартість: {g_cost}, калорії: {g_cal}")

    d_items, d_cost, d_cal = dynamic_programming(items, budget)
    print("Динамічне програмування:")
    print(f"  страви: {d_items}, вартість: {d_cost}, калорії: {d_cal}")