import re

with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('input.txt') as f:
  input = f.read().splitlines()

def p1(text):
  nums = [re.sub('[^\d]', '', line) for line in text]
  total = sum([int(n[0] + n[-1]) for n in nums])
  return total

def p2(text):
  # our input can have stuff like "oneight", which needs to be transformed into "18"
  text = [l.replace("eight", "eeight") for l in text]
  text = [l.replace("one", "oone") for l in text]
  text = [l.replace("two", "ttwo") for l in text]
  text = [l.replace("three", "tthree") for l in text]
  text = [l.replace("nine", "nnine") for l in text]
  numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  for i, t in enumerate(numbers):
    text = [l.replace(t, str(i + 1)) for l in text]
  return p1(text)

def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')

run(142, p1, test1)
run(281, p2, test2)
