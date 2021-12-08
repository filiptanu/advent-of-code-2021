input_file = open('input.txt', 'r')
crab_submarines = [int(i) for i in input_file.read().split('\n')[0].split(',') if i]

crab_positions = { i : 0 for i in crab_submarines }

for crab in crab_submarines:
  if not crab in crab_positions.keys():
    crab_positions[crab] = 1
  else:
    crab_positions[crab] += 1

total_fuel_for_position = { i : 0 for i in range(max(crab_submarines)) }

for target_position in total_fuel_for_position.keys():
  total_fuel = 0

  for current_position, number_of_crabs_at_current_position in crab_positions.items():
    difference = abs(current_position - target_position)
    fuel_for_single_crab = sum([i for i in range(1, difference + 1)])
    total_fuel += number_of_crabs_at_current_position * fuel_for_single_crab
  
  total_fuel_for_position[target_position] = total_fuel

print(min(total_fuel_for_position.values()))
