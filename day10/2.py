input_file = open('input.txt', 'r')
navigation = [i for i in input_file.read().split('\n') if i]

valid_navigation = []
scores = []

for line in navigation:
  stack = []
  invalid = False
  current_score = 0

  for char in line:
    if char == "(" or char == "[" or char == "{" or char == "<":
      stack.append(char)
    else:
      top_element = stack.pop()

      if top_element != "(" and char == ")":
        invalid = True
        break
      elif top_element != "[" and char == "]":
        invalid = True
        break
      elif top_element != "{" and char == "}":
        invalid = True
        break
      elif top_element != "<" and char == ">":
        invalid = True
        break
  
  if not invalid and stack != []:
    while stack != []:
      top_element = stack.pop()

      if top_element == "(":
        current_score = current_score * 5 + 1
      elif top_element == "[":
        current_score = current_score * 5 + 2
      elif top_element == "{":
        current_score = current_score * 5 + 3
      elif top_element == "<":
        current_score = current_score * 5 + 4
  
  if current_score != 0:
    scores.append(current_score)

scores.sort(reverse = True)

print(scores[int((len(scores) / 2))])
