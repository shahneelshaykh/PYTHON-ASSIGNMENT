def factorize_number(number):
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number = number // 2


    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number = number // i


    if number > 1:
        factors.append(number)

    return factors

num = int(input("Enter a number to factorize: "))
factors = factorize_number(num)

if len(factors) == 0:
    print(f"{num} is a prime number.")
else:
    print(f"Prime factors of {num}: {factors}")
