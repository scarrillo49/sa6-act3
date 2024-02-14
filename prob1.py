def sum_of_digits(number):
  number_str = str(number)

  sum_of_digits = sum(map(lambda digit: int(digit), number_str))

  return sum_of_digits

numbers = [123, 4567, 89012]
for number in numbers:
  print(f"Sum of digits of {number} is {sum_of_digits(number)}")