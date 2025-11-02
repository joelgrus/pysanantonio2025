def fizz_buzz(n):
    if n % 4 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 4 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)