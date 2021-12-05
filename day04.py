import copy
import re
import sys

import utils

def bingo(card, n, part=1):
    print('Bingo!')
    total = 0
    for row in card:
        total += sum([val for (val, status) in row if status == False])

    print(f"Part {part}: {total * n}")
    # Cheat's exit to save worrying about breaks
    if part == 2:
        sys.exit(0)


test_mode = len(sys.argv) > 1
input_file = f'day04_test_input.txt' if test_mode else f'day04_input.txt'
data = utils.input_as_lines(input_file)

called_numbers = [int(n) for n in data.pop(0).split(',')]
cards = []
card = []

for line in data:
    if line.strip() == '':
        if card:
            cards.append(card)
        card = []
    else:
        numbers = re.findall(r'(\d+) *', line)
        card.append([[int(n), False] for n in numbers])

if card:
    cards.append(card)

cards2 = copy.deepcopy(cards)

# Part 1
for n in called_numbers:
    for c_i, card in enumerate(cards):
        col_bingo = [True] * len(card)
        for row in card:
            row_bingo = True
            for i, [val, status] in enumerate(row):
                if val == n:
                    row[i][1] = True

                if row[i][1] == False:
                    row_bingo = False
                    col_bingo[i] = False

            if row_bingo:
                bingo(card, n)
                break
        else:
            if any(col_bingo):
                bingo(card, n)
                break
            continue
        break

    else:
        continue
    break

# Part 2
card_indices = list(range(len(cards2)))
for n in called_numbers:
    for c_i, card in enumerate(cards2):
        col_bingo = [True] * len(card)
        for row in card:
            row_bingo = True
            for i, [val, status] in enumerate(row):
                if val == n:
                    row[i][1] = True

                if row[i][1] == False:
                    row_bingo = False
                    col_bingo[i] = False

            if row_bingo:
                if c_i in card_indices:
                    if len(card_indices) == 1:
                        bingo(card, n, 2)
                    else:
                        card_indices.remove(c_i)

        else: # executed unless break out of row loop
            if any(col_bingo):
                if c_i in card_indices:
                    if len(card_indices) == 1:
                        bingo(card, n, 2)
                    else:
                        card_indices.remove(c_i)
