# https://adventofcode.com/2021/day/1

import sys

input = []
for line in sys.stdin:
    input.append(int(line))

# Part One
last = None
increases = 0
for item in input:
    if last is not None and item > last:
        increases += 1
    last = item

print(f"Part One: {increases}")

# Part Two
window = 3
increases = 0
start = 0
while (start + window) < len(input):
    a = sum(input[start:start + window])
    b = sum(input[start + 1:start + window + 1])
    if b > a:
        increases += 1
    start +=1

print(f"Part Two: {increases}")
