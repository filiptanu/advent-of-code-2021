from board import Board

input_file = open('input.txt', 'r')
bingo_data = [i for i in input_file.read().split('\n') if i]

drawn_numbers = bingo_data.pop(0).split(',')

boards = []

while(len(bingo_data) > 0):
  board_data = []

  for i in range(5):
    row = bingo_data.pop(0).split()
    board_data.append(row)
  
  boards.append(Board(board_data))

for number in drawn_numbers:
  for board in boards:
    board.mark(number)

    if board.has_won():
      print(board.score() * int(number))
      break
  else:
    continue
  break
