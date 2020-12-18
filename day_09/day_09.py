# Checks if list contains 2 items where item1 + item2 == sum
def has_sum_items(list, sum):
  l = 0
  r = len(list) - 1
  sorted_list = sorted(list, reverse=True)
  while(l < r):
    if (sorted_list[l] + sorted_list[r] == sum):
      return sorted_list[l], sorted_list[r]
    if (l == r - 1):
      l = 0
      r -= 1
    else:
      l += 1
  return False

def find_contiguous_set(list, sum):
  prev_index = 0
  current_index = 0
  local_sum = 0
  while (local_sum != sum and (current_index) < len(list) - 1):
    local_sum += list[current_index]
    if (local_sum > sum):
      local_sum = 0
      current_index = prev_index
      prev_index += 1
    else:
      current_index += 1
  return list[prev_index-1:current_index]


with open('input.txt', 'r') as file:
  lines = file.read().split('\n')
  numbers = list(map(lambda l: int(l), lines))

  preamble_length = 25
  index = 0
  has_sum = False
  wrong_number = None

  while (index + preamble_length <= len(numbers)):
    has_sum = has_sum_items(
        numbers[index:index+preamble_length], numbers[index+preamble_length])

    if (has_sum):
      index += 1
    else:
      wrong_number = numbers[index+preamble_length]
      print('Part 1: ' + str(wrong_number))
      contiguous_numbers = find_contiguous_set(numbers, wrong_number)
      print('Part 2: ' + str(min(contiguous_numbers) + max(contiguous_numbers)))
      break
