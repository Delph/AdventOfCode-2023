import math
import re

with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('input.txt') as f:
  input = f.read().splitlines()

def p1(text):
  total = 0
  for y, line in enumerate(text):
    x = 0
    while x < len(line):
      if line[x].isdigit():
        start = x
        while x < len(line) and line[x].isdigit():
          x += 1
        part_number = int(line[start:x])
        # find an adjacent symbol
        for i in range(y - 1, y + 2):
          if i < 0 or i >= len(text):
            continue
          for j in range(start - 1, x + 1):
            if j < 0 or j >= len(line):
              continue
            if text[i][j] != '.' and text[i][j].isdigit() == False:
              total += part_number
      x += 1
  return total

def p2(text):
  total = 0
  gears = {}
  for y, line in enumerate(text):
    x = 0
    while x < len(line):
      if line[x].isdigit():
        start = x
        while x < len(line) and line[x].isdigit():
          x += 1
        part_number = int(line[start:x])
        # find an adjacent symbol
        for i in range(y - 1, y + 2):
          if i < 0 or i >= len(text):
            continue
          for j in range(start - 1, x + 1):
            if j < 0 or j >= len(line):
              continue
            if text[i][j] == '*':
              label = f'{i}x{j}'
              if not label in gears:
                gears[label] = []
              gears[label].append(part_number)
      x += 1
  return sum(math.prod(g[1]) for g in gears.items() if len(g[1]) == 2)

def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')

run(4361, p1, test1)
run(467835, p2, test2)
