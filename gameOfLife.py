import random
import time

class cell:

  def __init__(self, isAlive):
    self.alive = isAlive

  def isAlive(self):
    return self.alive

  def setLife(self, alive):
    self.alive = alive

class board:
  def __init__(self, size): #min size  = 3
    self.size = size
    self.cells = [[0 for x in range(size)] for x in range(size)]

  def genBoard(self):
    for i in range(self.size):
      for j in range(self.size):
        x = random.randint(0,1)
        if x == 1:
          self.cells[i][j] = cell(True)
        else:
          self.cells[i][j] = cell(False)

  def printBoard(self):
    for i in range(self.size):
      for j in range(self.size):
        if self.cells[i][j].isAlive():
          print("x", end="")
        else:
          print("o", end="")
      print("\n", end="")
    for i in range(self.size):
      print("-", end="")
    print("\n", end="")

  def iterateBoard(self):
    tempBoard = [[0 for x in range(self.size)] for x in range(self.size)]
    for i in range(self.size):
      for j in range(self.size):
        a = 0
        if i-1 >= 0 and j-1 >= 0:
          if self.cells[i-1][j-1].isAlive():
            a += 1
        if i-1 > 0:
          if self.cells[i-1][j].isAlive():
            a += 1
        if i-1 >= 0 and j+1 < self.size:
          if self.cells[i-1][j+1].isAlive():
            a += 1
        if j-1 >= 0:
          if self.cells[i][j-1].isAlive():
            a += 1
        if j+1 < self.size:
          if self.cells[i][j+1].isAlive():
            a += 1
        if i+1 < self.size and j-1 >= 0:
          if self.cells[i+1][j-1].isAlive():
            a += 1
        if i+1 < self.size:
          if self.cells[i+1][j].isAlive():
            a += 1
        if i+1 < self.size and j+1 < self.size:
          if self.cells[i+1][j+1].isAlive():
            a += 1

        if self.cells[i][j].isAlive() and (a == 2 or a == 3):
          tempBoard[i][j] = cell(True)
        elif not self.cells[i][j].isAlive() and (a == 3):
          tempBoard[i][j] = cell(True)
        else:
          tempBoard[i][j] = cell(False)
    for i in range(self.size):
      for j in range(self.size):
        self.cells[i][j] = tempBoard[i][j]

  def simGame(self, iterations, delay):
    self.printBoard()
    for i in range(iterations):
      self.iterateBoard()
      self.printBoard()
      time.sleep(delay)

myBoard = board(10)
myBoard.genBoard()
myBoard.simGame(10, 5)
