input_file = open('input.txt', 'r')
navigation = [i for i in input_file.read().split('\n') if i]

points = 0

for line in navigation:
  stack = []

  for char in line:
    if char == "(" or char == "[" or char == "{" or char == "<":
      stack.append(char)
    else:
      top_element = stack.pop()

      if top_element != "(" and char == ")":
        points += 3
        break
      elif top_element != "[" and char == "]":
        points += 57
        break
      elif top_element != "{" and char == "}":
        points += 1197
        break
      elif top_element != "<" and char == ">":
        points += 25137
        break

print(points)
