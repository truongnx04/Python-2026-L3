#Write a Python function to calculate the factorial of a number (non-
#negative integer). The function accept the number as an argument.
def factorial(number):
    result = 1
    for value in range(1, number +1):
        result *= value

    return result

print(factorial(4))  # 24
print(factorial(0))  # 1   
        