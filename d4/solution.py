import re
import json

with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('input.txt') as f:
  input = f.read().splitlines()

def p1(text):
  total = 0
  for line in text:
    game = -1
    while '  ' in line:
      line = line.replace('  ', ' ')
    card, picks = line.split(': ')[1].split(' | ')
    card = sorted([int(c.strip()) for c in card.split(' ')])
    picks = sorted([int(c.strip()) for c in picks.split(' ')])
    for c in card:
      if c in picks:
        game += 1
    if game >= 0:
      total += 2 ** game
  return total

def p2(text):
  total = 0
  bonuses = []
  for line in text:
    while '  ' in line:
      line = line.replace('  ', ' ')
    card, picks = line.split(': ')[1].split(' | ')
    card = sorted([int(c.strip()) for c in card.split(' ')])
    picks = sorted([int(c.strip()) for c in picks.split(' ')])
    count = 0
    for c in card:
      if c in picks:
        count += 1
    # now we know how many we won, grant the extras
    bonus = 1
    if len(bonuses) > 0:
      bonus, *bonuses = bonuses
    for i in range(count):
      if i < len(bonuses):
        bonuses[i] += bonus
      else:
        bonuses.append(1 + bonus)
    total += bonus

  return total

def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')

run(13, p1, test1)
run(30, p2, test2)
