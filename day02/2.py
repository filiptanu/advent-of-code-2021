input_file = open('input.txt', 'r')
course = [i for i in input_file.read().split('\n') if i]

position = 0
depth = 0
aim = 0

for step in course:
  command, magnitude = step.split(' ')
  magnitude = int(magnitude)
  
  if command == 'forward':
    position += magnitude
    depth += aim * magnitude
  elif command == 'down':
    aim += magnitude
  elif command == 'up':
    aim -= magnitude

print(position * depth)
