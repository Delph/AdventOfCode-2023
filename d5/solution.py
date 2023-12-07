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


def parse_map(text, line):
  mapping = []

  while line < len(text) and text[line] != '':
    [destination, source, length] = map(int, text[line].split())
    mapping.append({'source': source, 'destination': destination, 'length': length})
    line += 1
  return sorted(mapping, key=lambda m: m['source']), line


def parse(text):
  seeds = list(map(int, text[0].split(': ')[1].split()))
  soil, line = parse_map(text, 3)
  fertilizer, line = parse_map(text, line + 2)
  water, line = parse_map(text, line + 2)
  light, line = parse_map(text, line + 2)
  temperature, line = parse_map(text, line + 2)
  humidity, line = parse_map(text, line + 2)
  location, line = parse_map(text, line + 2)
  return {
    'seeds': seeds,
    'maps': [soil, fertilizer, water, light, temperature, humidity, location]
  }

def resolve(source, mapping):
  for m in mapping:
    if source >= m['source'] and source <= m['source'] + m['length']:
      return source - m['source'] + m['destination']
  return source

def resolve_range(rng, mapping):
  new_maps = []
  # if rng[1] < mapping[0]['source']:
  # for m in mapping:
  #   if rng[1] < m[]


def p1(text):
  data = parse(text)

  locations = []
  for n in data['seeds']:
    for m in data['maps']:
      n = resolve(n, m)
    locations.append(n)
  return min(locations)


def p2(text):
  data = parse(text)

  location = math.inf
  for start, end in chunk(data['seeds'], 2):
    print(f'{start} {end}')
    for n in range(start, start + end):
      for m in data['maps']:
        n = resolve(n, m)
      if n < location:
        location = n
  return location



def run(expected, part, test):
  print(f'{part.__name__}:')
  test_result = part(test)
  if test_result == expected:
    print(f'\tTEST PASSED: {test_result} == {expected}')
    print(f'\tINPUT: {part(input)}')
  else:
    print(f'\tTEST FAILED: {test_result} != {expected}')


print(resolve_range((0, 10000), [{'source': 500, 'destination': 2000, 'length': 500}]))
# run(35, p1, test1)
# run(46, p2, test2)
