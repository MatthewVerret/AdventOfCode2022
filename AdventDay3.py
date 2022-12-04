from typing import List

from ReadFile import read_files

# ord() permet de savoir la valeur en ASCII
backpacks: List[str] = read_files("Backpacks.txt")

def day3_part1(bp: List[str]) -> int:
    p_sum: int = 0
    for i in bp:
        comp_1 = i[:len(i) // 2]
        comp_2 = i[len(i) // 2:]
        for j in range(len(comp_1)):
            if comp_1[j] in comp_2 and comp_1[j].isupper():
                p_sum += ord(comp_1[j]) - ord('A') + 27
                break
            if comp_1[j] in comp_2 and comp_1[j].islower():
                p_sum += ord(comp_1[j]) - ord('a') + 1
                break
    return p_sum

def day3_part2(bp: List[str]) -> int:
    p_sum: int = 0
    for i in range(0, len(bp), 3):
        for j in range(len(bp[i])):
            if bp[i][j] in bp[i + 1] and bp[i][j] in bp[i + 2] and bp[i][j].isupper():
                p_sum += ord(bp[i][j]) - ord('A') + 27
                break
            if bp[i][j] in bp[i + 1] and bp[i][j] in bp[i + 2] and bp[i][j].islower():
                p_sum += ord(bp[i][j]) - ord('a') + 1
                break
    return p_sum

print(day3_part1(backpacks))
print(day3_part2(backpacks))