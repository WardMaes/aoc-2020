
def check_password_1(min, max, char, passw):
  occurrences = passw.count(char)
  if (occurrences < min or occurrences > max):
    return 0
  else:
    return 1


def check_password_2(idx1, idx2, char, passw):
  char_at_idx1 = passw[idx1 - 1]
  char_at_idx2 = passw[idx2 - 1]

  if ((char_at_idx1 == char or char_at_idx2 == char) and char_at_idx1 != char_at_idx2):
    return 1
  else:
    return 0


with open('input.txt') as file:
  lines = file.read().split('\n')
  valid_passwords_1 = 0
  valid_passwords_2 = 0

  for line in lines:
    [range, middle, passw] = line.split(' ')
    [nr1, nr2] = range.split('-')
    [char, _] = middle.split(':')

    # Part 1
    valid_passwords_1 += check_password_1(int(nr1), int(nr2), char, passw)

    # Part 2
    valid_passwords_2 += check_password_2(int(nr1), int(nr2), char, passw)

  print('Part 1:', valid_passwords_1)
  print('Part 2:', valid_passwords_2)
