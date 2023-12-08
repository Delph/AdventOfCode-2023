import re
import json
import math
from functools import reduce


with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('input.txt') as f:
  input = f.read().splitlines()


def dumps(d):
  print(json.dumps(d, indent=2))


def chunk(l: list, n: int):
  n = max(1, n)
  return (l[i:i + n] for i in range(0, len(l), n))


def lcm(iterable):
  return reduce(lambda x, y: (x * y) // math.gcd(x,y), iterable)


def route(lr, d, start, end):
  p = start
  s = 0
  while p != end:
    p = d[p][0 if lr[s % len(lr)] == 'L' else 1]
    s += 1
  return s


def p1(text):
  lr, _, *d = text
  d = {p[0:3]: [p[7:10], p[12:15]] for p in d}
  return route(lr, d, 'AAA', 'ZZZ')


def p2(text):
  lr, _, *d = text
  d = {p[0:3]: [p[7:10], p[12:15]] for p in d}

  starts = list([s for s in d.keys() if s[-1] == 'A'])

  steps = 0
  cycles = []
  while True:
    starts = [d[s][0 if lr[steps % len(lr)] == 'L' else 1] for s in starts]
    if any(s for s in starts if s[-1] == 'Z'):
      cycles.append(steps + 1)
    if len(cycles) == len(starts):
      break
    steps += 1
  return lcm(cycles)


def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')


def dassert(actual, expected):
  if actual != expected:
    print(f'Expected {expected}, got {actual}')
    assert False


run(6, p1, test1)
run(6, p2, test2)
