
def group_answers(group):
  values = {}
  persons = group.split('\n')

  for person in persons:
    for answer in person:
      if answer in values:
        values[answer] += 1
      else:
        values[answer] = 1
  return values


def unique_answers(group):
  grouped = group_answers(group)
  return len(grouped.keys())


def unanimous_answers(groups):
  amount = 0
  for group in groups:
    grouped = group_answers(group)
    persons_in_group = len(group.split('\n'))

    print('grouped', grouped)

    for answer in grouped:
      if (grouped[answer] == persons_in_group):
        print(answer, grouped[answer])
        amount += 1

  return amount


with open('input.txt', 'r') as file:
  groups = file.read().split('\n\n')

  uniques = 0
  for group in groups:
    uniques += unique_answers(group)

  unanimous = unanimous_answers(groups)

  print('Part 1: ' + str(uniques))
  print('Part 2: ' + str(unanimous))
