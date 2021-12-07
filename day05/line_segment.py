class LineSegment:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
  
  def __repr__(self):
    return '(' + str(self.x1) + ', ' + str(self.y1) + ' -> ' + str(self.x2) + ', ' + str(self.y2) + ')'
  
  def is_horizontal(self):
    return self.y1 == self.y2
  
  def is_vertical(self):
     return self.x1 == self.x2
