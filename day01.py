import sys

import utils

test_mode = len(sys.argv) > 1
input_file = f'day01_test_input.txt' if test_mode else f'day01_input.txt'
data = utils.input_as_ints(input_file)

inc_count = 0
for i, n in enumerate(data):
    if i > 0:
        if n > data[i-1]:
            inc_count += 1

print(f"Part 1: {inc_count}")

inc_count = 0
prev_sum = 0
for i, n in enumerate(data):
    if i > 2:
        current_sum = sum([n, data[i-1], data[i-2]])
        if current_sum > prev_sum:
            inc_count += 1
        prev_sum = current_sum

print(f"Part 2: {inc_count}")
