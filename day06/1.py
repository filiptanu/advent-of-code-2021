input_file = open('input.txt', 'r')
lanternfish = [int(i) for i in input_file.read().split('\n')[0].split(',') if i]

for counter in range(80):
  current_lanternfish = lanternfish.copy()

  for index, fish in enumerate(current_lanternfish):
    if fish == 0:
      lanternfish.append(8)
      lanternfish[index] = 6
    else:
      lanternfish[index] -= 1

print(len(lanternfish))
