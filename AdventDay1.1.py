from typing import List

lines: List[str] = []
elfs_calories: List[int] = []
cal_value: int = 0

# Read the file
with open('CalorieCountingDay1.txt') as f:
    lines = f.read().splitlines()

for calories in lines:
    if calories == '':
        elfs_calories.append(cal_value)
        cal_value = 0
        continue
    cal_value += int(calories)

print(max(elfs_calories))