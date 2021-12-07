from line_segment import LineSegment

input_file = open('input.txt', 'r')
vent_data = [i for i in input_file.read().split('\n') if i]

lines = []
max_x = 0
max_y = 0

for line in vent_data:
  points = line.split(' -> ')
  point1 = points[0].split(',')
  x1 = int(point1[0])
  y1 = int(point1[1])
  point2 = points[1].split(',')
  x2 = int(point2[0])
  y2 = int(point2[1])

  if x1 > max_x:
    max_x = x1
  if y1 > max_y:
    max_y = y1

  if x2 > max_x:
    max_x = x2
  
  if y2 > max_y:
    max_y = y2

  lines.append(LineSegment(x1, y1, x2, y2))

max_x += 1
max_y += 1

board = [[0 for j in range(max_y)] for i in range(max_x)]

for line in lines:
  direction_x = -1 if line.x1 - line.x2 > 0 else 1
  direction_y = -1 if line.y1 - line.y2 > 0 else 1

  i = line.x1
  j = line.y1

  while True:
    board[j][i] += 1

    if i == line.x2 and j == line.y2:
      break

    if (i != line.x2):
      i += direction_x
    if (j != line.y2):
      j += direction_y

intersections = 0

for line in board:
  for cell in line:
    if cell > 1:
      intersections += 1

print(intersections)
