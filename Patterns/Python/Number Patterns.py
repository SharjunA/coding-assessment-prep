n = int(input("Enter the number if rows: "))
print()

#Pyramid of Numbers Pattern
print("Pyramid of Numbers Pattern")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end = " ")
    print()
print()
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
print()

#Inverted Numbers Pyramid Pattern
print("Inverted Numbers Pyramid Pattern")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(i, end = " ")
    print()
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
print()

#Inverted Half Pyramid Pattern
print("Inverted Half Pyramid Pattern")
for i in range(n, 1, -1):
    for j in range(0, i+1):
        print(j, end = " ")
    print()
print()