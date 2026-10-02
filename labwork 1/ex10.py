#Write a Python function get out all of divisors of a number.
def get_divisors(number):
    divisors = []

    for value in range(1, number + 1):
        if number % value == 0:
            divisors.append(value)

    return divisors

enter_num = int(input("Enter your number: "))
print(get_divisors(enter_num))        
