import re
import json
import math
from functools import reduce


with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('crow.txt') as f:
  input = f.read().splitlines()


def dumps(d):
  print(json.dumps(d, indent=2))


def chunk(l: list, n: int):
  n = max(1, n)
  return (l[i:i + n] for i in range(0, len(l), n))


def rank(hand, p2: bool = False):
  order = "J23456789TQKA" if p2 else "23456789TJQKA"
  r = 1
  for c in hand:
    r += order.index(c) + 1
    r *= 15
  return r


def strength(hand, p2: bool = False):
  s = {}
  for c in hand:
    if not c in s:
      s[c] = 0
    s[c] += 1

  counts = sorted([[card, count] for card,count in s.items()], key=lambda x: x[1], reverse=True)

  if p2:
    for i in range(len(counts)):
      if counts[i][0] != 'J':
        counts[i][1] += s['J'] if 'J' in s else 0
        counts = [c for c in counts if c[0] != 'J']
        break

  if counts[0][1] == 5:
    return 7
  if counts[0][1] == 4:
    return 6
  if counts[0][1] == 3:
    if counts[1][1] == 2:
      return 5
    return 4
  if counts[0][1] == 2:
    if math.prod(c for c in s.values()) == 4:
      return 3
    return 2
  return 1


def p1(text):
  hands = list(t.split() for t in text)
  hands = sorted(hands, key=lambda h: rank(h[0]))
  hands = sorted(hands, key=lambda h: strength(h[0]))
  return sum(int(h[1]) * (i + 1) for i, h in enumerate(hands))

def p2(text):
  hands = list(t.split() for t in text)
  hands = sorted(hands, key=lambda h: rank(h[0], True))
  hands = sorted(hands, key=lambda h: strength(h[0], True))
  return sum(int(h[1]) * (i + 1) for i, h in enumerate(hands))


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

dassert(strength('AAAAA'), 7)
dassert(strength('AAAAK'), 6)
dassert(strength('AAAKK'), 5)
dassert(strength('AAAKQ'), 4)
dassert(strength('AAKKQ'), 3)
dassert(strength('AAKQJ'), 2)
dassert(strength('AKQJT'), 1)

dassert(strength('AAAAA', True), 7)
dassert(strength('AAAAK', True), 6)
dassert(strength('AAAKK', True), 5)
dassert(strength('AAAKQ', True), 4)
dassert(strength('AAKKQ', True), 3)
dassert(strength('AAKQJ', True), 4)
dassert(strength('AKQJT', True), 2)
dassert(strength('JJKKA', True), 6)


run(6440, p1, test1)
run(5905, p2, test2)
