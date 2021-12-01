input_file = open('input.txt', 'r')
depths = [int(i) for i in input_file.read().split('\n') if i]

previous_depth = depths[0] + depths[1] + depths[2]
depth_increase_count = 0

for i, depth in enumerate(depths[3:], start=3):
  current_depth = depths[i] + depths[i - 1] + depths[i - 2]

  if current_depth > previous_depth:
    depth_increase_count += 1
  
  previous_depth = current_depth

print(depth_increase_count)
