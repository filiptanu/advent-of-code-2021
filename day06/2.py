input_file = open('input.txt', 'r')
lanternfish = [i for i in input_file.read().split('\n')[0].split(',') if i]

lanternfish_data = {}

for fish in lanternfish:
  if not fish in lanternfish_data.keys():
    lanternfish_data[fish] = 1
  else:
    lanternfish_data[fish] += 1

for counter in range(256):
  new_lanterfish_data = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0
  }

  for key, value in lanternfish_data.items():
    if key == '0':
      new_lanterfish_data['8'] += lanternfish_data['0']
      new_lanterfish_data['6'] += lanternfish_data['0']
    else:
      int_key = int(key)
      next_key = str(int_key - 1)
      new_lanterfish_data[next_key] += lanternfish_data[key]
    
  lanternfish_data = new_lanterfish_data

print(sum(lanternfish_data.values()))
