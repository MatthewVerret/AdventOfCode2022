from typing import List
from ReadFile import read_files
# A == Rock, B == Paper, C == Scissors -> Opponent
# X == Rock, Y == Paper, Z == Scissors -> You
#   1pts   ,     2pts  ,     3pts

lines: List[str] = read_files("RockPaperScissors.txt")

def day2_part1(lines: str) -> int:
    my_score: int = 0
    for i in lines:
        my_score += (('XYZ'.index(i[2]) - 'ABC'.index(i[0]) + 1) % 3 * 3) + ('XYZ'.index(i[2]) + 1)
    return my_score

def day2_part2(lines: str) -> int:
    my_score: int = 0
    for i in lines:
        if 'XYZ'.index(i[2]) == 0: # lost
            my_score += ('BCA'.index(i[0]) + 1)
        elif 'XYZ'.index(i[2]) == 1: # draw
            my_score += 3 + ('ABC'.index(i[0]) + 1)
        else: # win
            my_score += 6 + ('CAB'.index(i[0]) + 1)
    return my_score


print(day2_part1(lines))
print(day2_part2(lines))