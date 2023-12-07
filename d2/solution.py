import re
import json

with open('test1.txt') as f:
  test1 = f.read().splitlines()
with open('test2.txt') as f:
  test2 = f.read().splitlines()
with open('input.txt') as f:
  input = f.read().splitlines()

def p1(text):
  r, g, b = 12, 13, 14
  games = [re.split(r'[:;] ', g) for g in text]
  games = [{'id': int(g[0][4:]), 'pulls': g[1:]} for g in games]
  games = [{'id': g['id'], 'pulls': [p.split(', ') for p in g['pulls']]} for g in games]
  for game in games:
    pulls = []
    for pull in game['pulls']:
      rocks = [p.split(' ') for p in pull]
      pulls.append({r[1][0]: int(r[0]) for r in rocks})
    game['pulls'] = pulls
  total = 0
  for game in games:
    impossible = False
    for pull in game['pulls']:
      if pull.get('r', 0) > r or pull.get('g', 0) > g or pull.get('b', 0) > b:
        impossible = True
        break
    if impossible == False:
      total += game['id']
  return total

def p2(text):
  games = [re.split(r'[:;] ', g) for g in text]
  games = [{'id': int(g[0][4:]), 'pulls': g[1:]} for g in games]
  games = [{'id': g['id'], 'pulls': [p.split(', ') for p in g['pulls']]} for g in games]
  for game in games:
    pulls = []
    for pull in game['pulls']:
      rocks = [p.split(' ') for p in pull]
      pulls.append({r[1][0]: int(r[0]) for r in rocks})
    game['pulls'] = pulls
  total = 0

  for game in games:
    r = max([pull['r'] for pull in game['pulls'] if 'r' in pull])
    g = max([pull['g'] for pull in game['pulls'] if 'g' in pull])
    b = max([pull['b'] for pull in game['pulls'] if 'b' in pull])
    total += r * g * b

  return total

def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')

run(8, p1, test1)
run(2286, p2, test1)
