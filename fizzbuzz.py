for a in range(1, 200):
    if a % 7 == 0 and a % 9 == 0:
        print("FizzBuzz")
    elif a % 7 == 0:
        print("Fizz")
    elif a % 9 == 0:
        print("Buzz")
    else:
        print(a)