# https://adventofcode.com/2021/day/1
import sys


input = []
for line in sys.stdin:
    input.append(line)

horizontal = 0
depth = 0
for item in input:
    command, value = item.split()
    if command == 'forward':
        horizontal += int(value)
    elif command == 'up':
        depth -= int(value)
    elif command == 'down':
        depth += int(value)
    else:
        # unknown command
        pass

print(f'Part one {horizontal * depth}')

horizontal = 0
depth = 0
aim = 0
for item in input:
    command, value = item.split()
    if command == 'forward':
        horizontal += int(value)
        depth += int(value) * aim
    elif command == 'up':
        aim -= int(value)
    elif command == 'down':
        aim += int(value)
    else:
        # unknown command
        pass

print(f'Part two {horizontal * depth}')
