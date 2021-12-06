class Board:
  def __init__(self, data):
    self.data = data
    self.marked = [[False for j in range(5)] for i in range (5)]
  
  def __repr__(self):
    repr = ''

    for i in range(5):
      repr += ','.join(self.data[i])
      repr += '\n'
    
    return repr
  
  def mark(self, number):
    for i in range(5):
      for j in range(5):
        if self.data[i][j] == number:
          self.marked[i][j] = True
          break
      else:
        continue
      break
  
  def has_won(self):
    for i in range(5):
      if self.marked[i][0] == True and self.marked[i][1] == True and self.marked[i][2] == True and self.marked[i][3] == True and self.marked[i][4] == True:
        return True
    
    for i in range(5):
      if self.marked[0][i] == True and self.marked[1][i] == True and self.marked[2][i] == True and self.marked[3][i] == True and self.marked[4][i] == True:
        return True

  def score(self):
    sum = 0

    for i in range(5):
      for j in range(5):
        if self.marked[i][j] == False:
          sum += int(self.data[i][j])
    
    return sum
