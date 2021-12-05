import re
import sys

import utils

test_mode = len(sys.argv) > 1
input_file = f'day05_test_input.txt' if test_mode else f'day05_input.txt'
data = utils.input_as_string(input_file)

vents = [[int(s) for s in x] for x in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', data)]
max_x = max([v[0] for v in vents] + [v[2] for v in vents]) + 1
max_y = max([v[1] for v in vents] + [v[3] for v in vents]) + 1

# Part 1
line_counts = [[0]*max_y for i in range(max_x)]
for x1, y1, x2, y2 in vents:
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                line_counts[x][y] += 1

danger_count = 0
for line in line_counts:
    danger_count += len([i for i in line if i >= 2])

print(f'Part 1: {danger_count}')

# Part 2
line_counts = [[0]*max_y for i in range(max_x)]
for x1, y1, x2, y2 in vents:
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                line_counts[x][y] += 1
    else:
        start_x = min(x1, x2)
        for i in range(abs(x1 - x2)+1):
            if x2 > x1:
                x = x1 + i
            else:
                x = x1 - i
            if y2 > y1:
                y = y1 + i
            else:
                y = y1 - i
            line_counts[x][y] += 1

danger_count = 0
for line in line_counts:
    danger_count += len([i for i in line if i >= 2])

print(f'Part 2: {danger_count}')
