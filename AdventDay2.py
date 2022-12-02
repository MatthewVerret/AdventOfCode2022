from typing import List
from ReadFile import read_files
# A == Rock, B == Paper, C == Scissors -> Opponent
# X == Rock, Y == Paper, Z == Scissors -> You
#   1pts   ,     2pts  ,     3pts

lines: List[str] = read_files("RockPaperScissors.txt")

my_score: int = 0

for i in lines:
    opp_choice = 'ABC'.index(i[0])
    you_choice = 'XYZ'.index(i[2])
    comp = (you_choice - opp_choice + 1) % 3

    my_score += (comp * 3) + (you_choice + 1)


print(my_score)