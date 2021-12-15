input_file = open('input.txt', 'r')
rows = [i for i in input_file.read().split('\n') if i]

height_map = []

for index, row in enumerate(rows):
  height_map.append([int(i) for i in list(row) if i])

risk_levels_sum = 0

for i in range(len(height_map)):
  for j in range(len(height_map[i])):
    current_risk_level = 0

    if i == 0:
      if j == 0:
        if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]:
          current_risk_level += 1 + height_map[i][j]
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1]:
          current_risk_level += 1 + height_map[i][j]
      else:
        if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]:
          current_risk_level += 1 + height_map[i][j]
    elif i == len(height_map) - 1:
      if j == 0:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]:
          current_risk_level += 1 + height_map[i][j]
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1]:
          current_risk_level += 1 + height_map[i][j]
      else:
        if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]:
          current_risk_level += 1 + height_map[i][j]
    else:
      if j == 0:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i + 1][j]:
          current_risk_level += 1 + height_map[i][j]
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j]:
          current_risk_level += 1 + height_map[i][j]
      else:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i][j + 1]:
          current_risk_level += 1 + height_map[i][j]
    
    risk_levels_sum += current_risk_level

print(risk_levels_sum)
