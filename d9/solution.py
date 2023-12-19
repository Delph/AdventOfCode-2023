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

def steps(n):
  return [y-x for x,y in zip(n, n[1:])]


def p1(text):
  total = 0
  lines = [list(map(int, l.split())) for l in text]
  for line in lines:
    stack = [line]
    while any(x != 0 for x in stack[-1]):
      stack.append(steps(stack[-1]))
    stack[-1].append(0)
    while len(stack) > 1:
      stack[-2].append(stack[-2][-1] + stack[-1][-1])
      stack.pop()
    total += stack[0][-1]
  return total

def p2(text):
  total = 0
  lines = [list(map(int, l.split())) for l in text]
  for line in lines:
    stack = [line]
    while any(x != 0 for x in stack[-1]):
      stack.append(steps(stack[-1]))
    stack[-1] = [0, *stack[-1]]
    while len(stack) > 1:
      stack[-2] = [stack[-2][0] - stack[-1][0], *stack[-2]]
      stack.pop()
    total += stack[0][0]
  return total


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


run(114, p1, test1)
run(2, p2, test2)
