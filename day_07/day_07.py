import re


def dfs(color):
  for bag in bags:
    if(bag not in visited):
      if color in bags[bag]:
        visited.add(bag)
        dfs(bag)
  return visited


def dfs_2(bag):
  sum = 1
  if(bag in bags):
    for b in bags[bag]:
      multiplier = bags[bag][b]
      sum += multiplier * dfs_2(b)
  return sum


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')

  bags = {}
  for line in lines:
    bag = re.match(r'(.*) bags contain', line).groups()[0]
    for count, b in re.findall(r'(\d+) (\w+ \w+) bag', line):
      if not (bag in bags):
        bags[bag] = {}
      bags[bag][b] = int(count)

  visited = set()
  dfs('shiny gold')
  amount = dfs_2('shiny gold') - 1
  print('Part 1: ' + str(len(visited)))
  print('Part 2: ' + str(amount))
