n = int(input("Enter the number if rows: "))
print()

#Simple Half Pyramid Pattern
print("Simple Half Pyramid Pattern")
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print()
# print()

for i in range(1, n+1):
    print("* " * i)
print()

#Right Triangeled Pyramid
#print("Right Triangeled Pyramid Patterns")
# k = 2 * n - 2
# for i in range(0, n):
#     for j in range(0, k):
#         print(end = "")
#         k -= 1
#     for j in range(0, i+1):
#         print("* ", end = "")
#     print()
# print()

#Mirrored Right Triangle
print("Mirrored Right Triangle Pattern")
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end = " ")
    k -= 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
print()

#Downward Half-Pyramid Pattern
print("Downward Half-Pyramid Pattern")
# for i in range(n, -1, -1):
#     for j in range(0, i):
#         print("* ", end = "")
#     print()

for i in range(n, -1, -1):
    print("* " * i)

#Mirrored Downward Half Pyramid Pattern
print('Mirrored Downward Half Pyramid Pattern')
i = n
while i > 0:
    j = n
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
print()

#Full Pyramid Pattern
print("Full Pyramid Pattern")
k = 2 * n - 2
for i in range(0, n):    
    for j in range(0, k):    
        print(end = " ")    
    k -= 1   
    for j in range(0, i+1):    
        print("* ", end = "")
    print()  
print()


#Equilateral Triangle
print("Equilateral Triangle Pattern")
k = 2 * n - 2
for i in range(0, n):    
    for j in range(0, k):    
        print(end = " ")    
    k -= 1   
    for j in range(0, i + 1):    
        print("* ", end = " ")
    print()  
print()

#Downward Full Pyramid Pattern
k = 2 * n - 2
print("Downward Full Pyramid Pattern")
for i in range(n, -1, -1):
    for j in range(k, 0, -1):
        print(end = " ")
    k += 1
    for j in range(0, i+1):
        print("* ", end = "")
    print()
print()