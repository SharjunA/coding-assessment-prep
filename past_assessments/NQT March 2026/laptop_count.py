'''
Problem Statement: Laptops That Can Last the Meeting

A company is conducting an online meeting that will last for M minutes. Several employees bring their laptops to attend the meeting.
Each laptop has a certain battery level (in minutes) indicating how long it can operate without charging.
Your task is to determine how many laptops can last for the entire meeting without shutting down.
A laptop can be used for the meeting only if its battery level is greater than or equal to the meeting duration.

Input Format
The first line contains an integer M, representing the duration of the meeting (in minutes).
The second line contains space-separated integers representing the battery levels of the laptops (in minutes).

Output Format
Print a single integer representing the number of laptops that can last the entire meeting.
'''

meeting_duration = int(input())
laptop_battery_levels = list(map(int, input().split()))
laptop_count = 0

for battery in laptop_battery_levels:
    if battery >= meeting_duration:
        laptop_count += 1
        
print(laptop_count)