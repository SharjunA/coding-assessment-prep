meeting_duration = int(input())
laptop_battery_levels = list(map(int, input().split()))
laptop_count = 0

for battery in laptop_battery_levels:
    if battery >= meeting_duration:
        laptop_count += 1
        
print(laptop_count)