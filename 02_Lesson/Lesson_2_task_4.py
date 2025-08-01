def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


try:
    enter_number = int(input("Введите число от 0 до 99: "))
    print(fizz_buzz(enter_number))
except ValueError:
    print("Пожалуйста введите целое число 17.")
