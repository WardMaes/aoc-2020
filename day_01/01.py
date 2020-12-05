def get_tuple(arr, sum):
  # Returns a tuple. The sum of these 2 values equals sum
  arr_sorted = sorted(arr)
  l = 0
  r = len(arr) - 1

  while l < r:
    if (arr_sorted[l] + arr_sorted[r] == sum):
      return [arr_sorted[l], arr_sorted[r]]
    elif (arr_sorted[l] + arr_sorted[r] < sum):
      l += 1
    else:
      r -= 1
  return [-1, -1]


def get_triple(arr, sum):
  # Returns a triple. The sum of these 3 values equals sum
  arr_sorted = sorted(arr)
  i = 0
  l = 0
  r = len(arr) - 1

  while(l < r):
    val1, val2 = get_tuple(arr_sorted, sum - arr_sorted[i])
    if (val1 > -1):
      return arr_sorted[i], val1, val2
    else:
      l += 1
      i += 1
  return -1, -1, -1


lines = open("input.txt", "r")
strings = lines.read().splitlines()
numbers = list(map(int, strings))

# Part 1

val1, val2 = get_tuple(numbers, 2020)
print(val1, val2, " => ", val1 * val2)

# Part 2

v1, v2, v3 = get_triple(numbers, 2020)
print(v1, v2, v3, " => ", v1 * v2 * v3)
