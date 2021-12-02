import re
import sys

import utils

test_mode = len(sys.argv) > 1
input_file = f'day02_test_input.txt' if test_mode else f'day02_input.txt'
data = utils.input_as_string(input_file)

instructions = re.findall(r'(\w+) (\d+)', data)

# Part 1
x = 0
y = 0

for (dir, steps) in instructions:
    steps = int(steps)
    if dir == 'forward':
        x += steps
    elif dir == 'down':
        y += steps
    elif dir == 'up':
        y -= steps

print(f"Part 1: {(x * y)}")

# Part 2
x = 0
y = 0
aim = 0

for (dir, steps) in instructions:
    steps = int(steps)
    if dir == 'forward':
        x += steps
        y += steps * aim
    elif dir == 'down':
        aim += steps
    elif dir == 'up':
        aim -= steps

print(f"Part 2: {(x * y)}")
