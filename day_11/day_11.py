from copy import deepcopy


def get(seats, row, nr):
  if (row >= len(seats) or nr >= len(seats[row]) or row < 0 or nr < 0):
    return ''
  return seats[row][nr]


def adjacent(seats, row, nr):
  seats_around = [
      get(seats, row+1, nr),
      get(seats, row-1, nr),
      get(seats, row, nr-1),
      get(seats, row, nr+1),
      get(seats, row-1, nr-1),
      get(seats, row+1, nr+1),
      get(seats, row-1, nr+1),
      get(seats, row+1, nr-1),
  ]
  return seats_around.count('#')


def directions(seats, row, col):
  neibhour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
  nr_occupied = 0
  for dr, dc in neibhour_offsets:
    cr, cc = row + dr, col + dc
    while 0 <= cr < len(seats) and 0 <= cc < len(seats[row]) and seats[cr][cc] == '.':
      cr += dr
      cc += dc
    nr_occupied += 0 <= cr < len(seats) and 0 <= cc < len(
        seats[row]) and seats[cr][cc] == '#'

  return nr_occupied


def stabilize(model, amount):
  seats = deepcopy(og_seats)
  seats_copy = deepcopy(seats)
  done = False
  while (not done):
    done = True
    for rownr, row in enumerate(seats):
      for colnr, seat in enumerate(row):
        # Take seats
        if (seat == 'L' and model(seats, rownr, colnr) == 0):
          seats_copy[rownr][colnr] = '#'
          done = False
        # Leave seats
        elif (seat == '#' and model(seats, rownr, colnr) >= amount):
          seats_copy[rownr][colnr] = 'L'
          done = False
    seats = deepcopy(seats_copy)

  occupied = sum(row.count('#') for row in seats)
  return occupied


og_seats = [list(row) for row in open('input.txt').read().splitlines()]

part1 = stabilize(adjacent, 4)
print('Part 1: ' + str(part1))
part2 = stabilize(directions, 5)
print('Part 2: ' + str(part2))
