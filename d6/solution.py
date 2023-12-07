import re
import json
import math


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


def p1(text):
  times = map(int, text[0][10:].split())
  dists = map(int, text[1][10:].split())

  return math.prod(sum([1 for h in range(t) if h * (t - h) > d]) for t,d in zip(times, dists))


def p2(text):
  t = int(''.join(text[0][10:].split()))
  d = int(''.join(text[1][10:].split()))

  return sum([1 for h in range(t) if h * (t - h) > d])


def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')


run(288, p1, test1)
run(71503, p2, test2)
