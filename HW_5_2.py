# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь 
# с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии.

Employee = ["Boris", "Aleksey", "David", "Leo"]
Rate = [10000, 20000, 15000, 30000]
Bonus = ["10.25%", "7.14%", "11.50%", "14.65%"]


def gen_dict(employee: list[str], rate: list[int], bonus: list[str]):
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(employee, rate, map(lambda x: float(x[:-1]), bonus))))}


def main():
    print(Employee)
    print(Rate)
    print(Bonus)
    print(*gen_dict(Employee, Rate, Bonus))


if __name__ == "__main__":
    main()
