# 7. Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2. 
# Для проверки числа на простоту используйте правило: «число является простым, если делится 
# нацело только на единицу и на себя».

def prime_generator(n):
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            yield num
            prime_count += 1
        num += 1
        
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 10
primes = prime_generator(n)
for prime in primes:
    print(prime)
