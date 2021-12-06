def find_most_common_values(report):
  most_common_values = [0 for i in range(len(report[0]))]

  for entry in report:
    for index, character in enumerate(entry):
      if character == '1':
        most_common_values[index] += 1
      elif character == '0':
        most_common_values[index] -= 1
  
  return most_common_values


input_file = open('input.txt', 'r')
report = [i for i in input_file.read().split('\n') if i]

most_common_values = find_most_common_values(report)
oxygen_generator_rates = report.copy()
co2_scrubber_rates = report.copy()

for i in range(len(most_common_values)):
  if (len(oxygen_generator_rates) > 1):
    oxygen_most_common_values = find_most_common_values(oxygen_generator_rates)
    most_common_value = '1' if oxygen_most_common_values[i] >= 0 else '0'
    oxygen_generator_rates = list(filter(lambda entry: entry[i] == most_common_value, oxygen_generator_rates))

  if (len(co2_scrubber_rates) > 1):
    co2_most_common_values = find_most_common_values(co2_scrubber_rates)
    least_common_value = '1' if co2_most_common_values[i] < 0 else '0'
    co2_scrubber_rates = list(filter(lambda entry: entry[i] == least_common_value, co2_scrubber_rates))

oxygen_generator_rate = int(''.join(oxygen_generator_rates[0]), 2)
co2_scrubber_rate = int(''.join(co2_scrubber_rates[0]), 2)

print(oxygen_generator_rate * co2_scrubber_rate)
