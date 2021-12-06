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

last_winning_board = None
last_winning_number = 0

for number in drawn_numbers:
  for index, board in enumerate(boards):
    board.mark(number)

    if board.has_won():
      last_winning_board = board
      last_winning_number = number

  boards = [board for board in boards if not board.has_won()]

print(last_winning_board.score() * int(last_winning_number))
