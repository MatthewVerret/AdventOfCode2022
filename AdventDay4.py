from typing import List, Tuple
from ReadFile import read_files

lines : List[str] = read_files("Day4.txt")

def day4_part1(lines: List[str]) -> int:
    cpt: int = 0
    for i in lines:
        p: List[str] = i.split(',')
        t: Tuple[str] = p[0].split('-'), p[1].split('-')
        if (int(t[0][0]) >= int(t[1][0]) and int(t[0][1]) <= int(t[1][1]) 
            or int(t[0][0]) <= int(t[1][0]) and int(t[0][1]) >= int(t[1][1])):
            cpt += 1
    return cpt

def day4_part2(lines: List[str]) -> int:
    cpt: int = 0
    for i in lines:
        p: List[str] = i.split(',')
        t: Tuple[str] = p[0].split('-'), p[1].split('-')
        if (int(t[0][0]) <= int(t[1][0]) and int(t[0][1]) >= int(t[1][0]) 
            or int(t[1][0]) <= int(t[0][0]) and int(t[1][1]) >= int(t[0][0])):
            cpt += 1
    return cpt

print(day4_part1(lines))
print(day4_part2(lines))