number_of_people = int(input())

happy_people = number_of_people
sad_people = 0

for _ in range(4):
    from_happy_to_sad = int(round(happy_people * 0.7))
    from_sad_to_happy = sad_people//2
    
    happy_people -= (from_happy_to_sad - from_sad_to_happy)
    sad_people -= (from_sad_to_happy - from_happy_to_sad)
    
print(happy_people, sad_people)


'''
n = int(input())
happy = n
for _ in range(4):
    happy = int(round(0.5*n - 0.2*happy))
sad = n - happy
print(happy, sad)
'''
