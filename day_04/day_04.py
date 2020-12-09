import re


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_passport(passport):
  # Part 1
  if not all(key in passport for key in required_fields):
    return False

  # Part 2
  if not (1920 <= int(passport['byr']) <= 2002):
    return False

  if not (2010 <= int(passport['iyr']) <= 2020):
    return False

  if not (2020 <= int(passport['eyr']) <= 2030):
    return False

  if (passport['hgt'].endswith('cm')):
    if not (150 <= int(passport['hgt'][:-2]) <= 193):
      return False
  elif (passport['hgt'].endswith('in')):
    if not (59 <= int(passport['hgt'][:-2]) <= 76):
      return False
  else:
    return False

  hcl_pattern = re.compile('^#([a-f]|[0-9]){6}$')
  if not (hcl_pattern.match(passport['hcl'])):
    return False

  if not (passport['ecl'] in eye_colors):
    return False

  pid_pattern = re.compile('^([0-9]){9}$')
  if not (pid_pattern.match(passport['pid'])):
    return False

  return True


with open('input.txt', 'r') as file:
  passports = file.read().split('\n\n')
  valid_passports = []
  for pp in passports:
    pp = pp.replace('\n', ' ')
    passport = dict(field.split(':') for field in pp.split(' '))
    is_valid = is_valid_passport(passport)
    if (is_valid):
      valid_passports.append(passport)

  print(len(valid_passports))
