import math

# TODO: fix float vs int
def binary_search(sequence, min, max):
  part = sequence[:1]
  if (int(max - min) == 1):
    if (part == 'F' or part == 'L'):
      return min
    elif (part == 'B' or part == 'R'):
      return max

  if (part == 'F' or part == 'L'):
    return binary_search(sequence[1:], min, min + math.floor((max - min) / 2))
  elif (part == 'B' or part == 'R'):
    return binary_search(sequence[1:], min + math.ceil((max - min) / 2), max)


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')
  ids = []
  for line in lines:
    row = int(binary_search(line[:7], float(0), float(127)))
    column = int(binary_search(line[-3:], float(0), float(7)))
    id = row * 8 + column
    ids.append(id)


print('Part 1: ' + str(max(ids)))

sorted = sorted(ids)
for i in range(len(sorted)):
  if (sorted[i] != sorted[i - 1] + 1 and i > 0):
    print('Part 2: ' + str(sorted[i - 1] + 1))
