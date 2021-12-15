input_file = open('input.txt', 'r')
seven_segment_display_data = [i for i in input_file.read().split('\n') if i]

unique_signal_patterns = []
output_values = []

for data in seven_segment_display_data:
  pattern, value = data.split(' | ')
  unique_signal_patterns.append(pattern)
  output_values.append(value)

digit_instances = 0

for value in output_values:
  digits = value.split()

  for digit in digits:
    if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
      digit_instances += 1

print(digit_instances)
