def last_digit(num, exp):
    return pow(num, exp, 10)

num = 7
exp = 3
print(f"Last digit of {num}^{exp} is: {last_digit(num, exp)}")