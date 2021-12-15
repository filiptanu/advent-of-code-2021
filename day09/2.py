input_file = open('input.txt', 'r')
rows = [i for i in input_file.read().split('\n') if i]

height_map = []

for index, row in enumerate(rows):
  height_map.append([int(i) for i in list(row) if i])

low_points = []

for i in range(len(height_map)):
  for j in range(len(height_map[i])):
    if i == 0:
      if j == 0:
        if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]:
          low_points.append((i, j))
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1]:
          low_points.append((i, j))
      else:
        if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j + 1]:
          low_points.append((i, j))
    elif i == len(height_map) - 1:
      if j == 0:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]:
          low_points.append((i, j))
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1]:
          low_points.append((i, j))
      else:
        if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1]:
          low_points.append((i, j))
    else:
      if j == 0:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i + 1][j]:
          low_points.append((i, j))
      elif j == len(height_map[i]) - 1:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j]:
          low_points.append((i, j))
      else:
        if height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i][j + 1]:
          low_points.append((i, j))

def dfs(i, j, visited, basin_count):
  if visited[i][j] == 0:
    visited[i][j] = basin_count

    if i > 0:
      if height_map[i - 1][j] > height_map[i][j] and height_map[i - 1][j] != 9:
        dfs(i - 1, j, visited, basin_count)
    if i < len(visited) - 1:
      if height_map[i + 1][j] > height_map[i][j] and height_map[i + 1][j] != 9:
        dfs(i + 1, j, visited, basin_count)
    if j > 0:
      if height_map[i][j - 1] > height_map[i][j] and height_map[i][j - 1] != 9:
        dfs(i, j - 1, visited, basin_count)
    if j < len(visited[0]) - 1:
      if height_map[i][j + 1] > height_map[i][j] and height_map[i][j + 1] != 9:
        dfs(i, j + 1, visited, basin_count)

visited = [[0 for j in range(len(height_map[0]))] for i in range(len(height_map))]
basin_count = 1

for low_point in low_points:
  dfs(low_point[0], low_point[1], visited, basin_count)
  basin_count += 1

basin_to_size = {basin: 0 for basin in list(set(i for j in visited for i in j)) if basin > 0}

for basin in basin_to_size.keys():
  size = [i for j in visited for i in j if i == basin].count(basin)
  basin_to_size[basin] = size

basin_sizes = list(basin_to_size.values())
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
