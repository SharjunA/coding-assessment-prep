def is_leap(year):
    if year%400 == 0 or (year%4 ==0 and year%100 != 0):
        return True
    return False

year = 2020
print(f"Is {year} a leap year? {is_leap(year)}")