input_file = open('input.txt', 'r')
crab_submarines = [int(i) for i in input_file.read().split('\n')[0].split(',') if i]

crab_positions = {}

for crab in crab_submarines:
  if not crab in crab_positions.keys():
    crab_positions[crab] = 1
  else:
    crab_positions[crab] += 1

total_fuel_for_position = { i : 0 for i in crab_submarines }

for position in total_fuel_for_position.keys():
  total_fuel = 0

  for key, value in crab_positions.items():
    total_fuel += value * abs(key - position)
  
  total_fuel_for_position[position] = total_fuel

print(min(total_fuel_for_position.values()))
