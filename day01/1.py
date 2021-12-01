input_file = open('input.txt', 'r')
depths = [int(i) for i in input_file.read().split('\n') if i]

previous_depth = depths[0]
depth_increase_count = 0

for current_depth in depths[1:]:
  if current_depth > previous_depth:
    depth_increase_count += 1
  
  previous_depth = current_depth

print(depth_increase_count)
