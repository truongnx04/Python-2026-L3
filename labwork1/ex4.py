# Write a program that checks whether a number is perfect or not.
number = int(input("Enter a number: "))
sum_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_divisors += i

if number == sum_divisors:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is a not perfect number")
        