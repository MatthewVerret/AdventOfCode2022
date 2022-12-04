from typing import List
from ReadFile import read_files

# Read the file
lines: List[str] = read_files('Day1.txt')

def sorted_calories(list: List):
    elfs_calories: List[int] = []
    cal_value: int = 0
    for calories in list:
        if calories == '':
            elfs_calories.append(cal_value)
            cal_value = 0
            continue
        cal_value += int(calories)
    
    return sorted(elfs_calories, reverse=True)

print(max(sorted_calories(lines)))
print(sum(sorted_calories(lines)[0:3]))