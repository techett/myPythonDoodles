import tkinter
import random

game_symbols = {1: "Cherry",
                2: "Orange",
                3: "Banana",
                4: "Watermelon",
                5: "Kiwi",
                6: "Lime",
                7: "Lemon",
                8: "Straw Berry",
                9: "Black Berry",
                10: "Apricot",
                11: "Apple",
                12: "Coconut",
                13: "Cucumber",
                14: "Durian",
                15: "Dragonfruit",
                16: "Fig",
                17: "Gooseberry",
                18: "Grape",
                19: "Guava",
                20: "Jackfruit"}


# Function needed to reduce lines.
line_one = [random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values()))]

line_two = [random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values())),
            random.choice(list(game_symbols.values()))]

line_three = [random.choice(list(game_symbols.values())),
              random.choice(list(game_symbols.values())),
              random.choice(list(game_symbols.values())),
              random.choice(list(game_symbols.values()))]

print(line_one)
print(line_two)
print(line_three)


# will need to move functions
def check_win_single_line(line_one):
    if line_one[0] == line_one[1] == line_one[2] == line_one[3]:
        print("Small win!")


def check_win_vertical_left(top, middle, bottom):
    if top[0] == middle[0] == bottom[0]:
        print("Winner on vertical left!")


def check_win_vertical_middle(top, middle, bottom):
    if top[1] == middle[1] == bottom[1]:
        print("Winner on vertical middle!")


def check_win_vertical_right(top, middle, bottom):
    if top[2] == middle[2] == bottom[2]:
        print("Winner on vertical right")


check_win_single_line(line_one)
check_win_single_line(line_two)
check_win_single_line(line_three)

check_win_vertical_left(line_one, line_two, line_three)
check_win_vertical_middle(line_one, line_two, line_three)
check_win_vertical_right(line_one, line_two, line_three)
