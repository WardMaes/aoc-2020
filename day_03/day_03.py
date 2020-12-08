import math

def count_trees(lines, x, y):
  y_pos = 0
  x_pos = 0
  elements = []
  while (y_pos < len(lines)):
    line = lines[y_pos]
    line_length = len(line)
    element = line[x_pos % line_length]
    elements.append(element)
    x_pos += x
    y_pos += y

  return elements.count('#')


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')
  amounts = []
  amounts.append(count_trees(lines, 1, 1))
  amounts.append(count_trees(lines, 3, 1))
  amounts.append(count_trees(lines, 5, 1))
  amounts.append(count_trees(lines, 7, 1))
  amounts.append(count_trees(lines, 1, 2))

  print(math.prod(amounts))
