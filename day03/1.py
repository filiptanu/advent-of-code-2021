input_file = open('input.txt', 'r')
report = [i for i in input_file.read().split('\n') if i]

most_common_values = [0 for i in range(len(report[0]))]

for entry in report:
  for index, character in enumerate(entry):
    if character == '1':
      most_common_values[index] += 1
    elif character == '0':
      most_common_values[index] -= 1

gamma_rate = ['0' for i in range(len(report[0]))]
epsilon_rate = ['0' for i in range(len(report[0]))]

for index, frequency in enumerate(most_common_values):
  if frequency > 0:
    gamma_rate[index] = '1'
    epsilon_rate[index] = '0'
  else:
    gamma_rate[index] = '0'
    epsilon_rate[index] = '1'

gamma_rate = int(''.join(gamma_rate), 2)
epsilon_rate = int(''.join(epsilon_rate), 2)

print(gamma_rate * epsilon_rate)
