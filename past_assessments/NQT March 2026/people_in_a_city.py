'''
Problem Statement: Happy and Sad People Simulation

In a town, there are N people, all of whom are initially happy. Over time, people's emotions change according to the following rules:

In each round, 70% of the happy people become sad.
At the same time, 50% of the sad people become happy.

The changes happen simultaneously in each round.

Your task is to simulate this process for 4 rounds and determine the number of happy and sad people remaining at the end.

Input Format:
A single integer N representing the total number of people.

Output Format:
Print two integers separated by a space:
The number of happy people
The number of sad people

Notes
The number of people transitioning between states should be rounded to the nearest integer when calculating 70% of happy people.
For the sad people becoming happy, exactly half of the sad people transition (integer division may be used).
The total number of people remains constant throughout the simulation.
'''


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
