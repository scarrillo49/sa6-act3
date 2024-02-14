def find_max(numbers, greater):
  maximum = numbers[0]

  for number in numbers[1:]:
    maximum = greater(maximum, number)

  return maximum

numbers = [3, 8, 2, 30, 29]
greater = lambda x, y: x if x > y else y

max_number = find_max(numbers, greater)
print(max_number)
