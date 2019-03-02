def is_prime():
    for num in range(2, 101):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num, "is prime")


for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", number)
    elif number % 3 == 0:
        print("fizz", number)
    elif number % 5 == 0:
        print("buzz", number)
    else:
        print(number)

