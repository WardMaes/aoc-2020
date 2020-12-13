def flip_op(val):
  return 'jmp' if val == 'nop' else 'nop'


def run(program):
  ip = 0
  acc = 0
  executed = []

  while (ip not in executed and ip >= 0):

    if (ip > len(program) - 1):
      break

    executed.append(ip)
    instruction = program[ip]

    if (instruction['op'] == 'nop'):
      ip += 1
      continue

    if (instruction['op'] == 'acc'):
      acc += instruction['arg']
      ip += 1
      continue

    if (instruction['op'] == 'jmp'):
      ip += instruction['arg']
      continue

    print('invalid instruction', instruction['op'])

  return ip, acc


def update_program(program):
  for idx, instruction in enumerate(program):

    if instruction['op'] == 'nop' or instruction['op'] == 'jmp':
      original_op = instruction['op']
      program[idx]['op'] = flip_op(instruction['op'])
      ip, acc = run(program)

      if (ip == len(program)):
        return ip, acc

      program[idx]['op'] = original_op


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')

  program = []
  for instruction in lines:
    operation, argument = instruction.split(' ')
    instruction = {}
    instruction['op'] = operation
    instruction['arg'] = int(argument)
    program.append(instruction)

  # Part 1
  ip, acc = run(program)
  print('Part 1: ' + str(acc))

  # # Part 2
  ip, acc = update_program(program)
  print('Part 2: ' + str(acc))
