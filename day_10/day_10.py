from collections import defaultdict


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')
  sorted_adapters = sorted(map(int, lines))

  sorted_adapters.insert(0, 0)  # from 0
  differences_of_1 = 0
  differences_of_3 = 0

  for index, adapter in enumerate(sorted_adapters):
    if (index + 1 < len(sorted_adapters)):
      diff = sorted_adapters[index + 1] - sorted_adapters[index]
      if (diff > 3):
        break
      if (diff == 1):
        differences_of_1 += 1
      elif (diff == 3):
        differences_of_3 += 1

  differences_of_3 += 1  # to charger

  print('Part 1: ' + str(differences_of_1 * (differences_of_3)))

  paths = defaultdict(int)
  paths[0] = 1
  for adapter in sorted_adapters:
    for diff in range(1, 4):
      next_adapter = adapter + diff
      if next_adapter in sorted_adapters:
        paths[next_adapter] += paths[adapter]

  print('Part 2: ' + str(paths[max(sorted_adapters)]))
