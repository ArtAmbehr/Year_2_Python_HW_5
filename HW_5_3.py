# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию).
#  Первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел

def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for i in range(15):
    print(next(fib))