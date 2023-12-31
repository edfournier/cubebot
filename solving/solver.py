import numpy as np
import py222

hO = np.ones(729, dtype=int) * 12
hP = np.ones(117649, dtype=int) * 12

moveStrs = {0: "U", 1: "U'", 2: "U2", 3: "R", 4: "R'", 5: "R2", 6: "F", 7: "F'", 8: "F2"}

# generate pruning table for the piece orientation states
def genOTable(s, d, lm=-3):
  index = py222.indexO(py222.getOP(s))
  if d < hO[index]:
    hO[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genOTable(py222.doMove(s, m), d + 1, m)

# generate pruning table for the piece permutation states
def genPTable(s, d, lm=-3):
  index = py222.indexP(py222.getOP(s))
  if d < hP[index]:
    hP[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genPTable(py222.doMove(s, m), d + 1, m)
    
solutions = []

# IDA* which prints all optimal solutions
def IDAStar(s, d, moves, lm=-3):
  if py222.isSolved(s):
    solutions.append(stringify(moves))
    return True
  else:
    sOP = py222.getOP(s)
    if d > 0 and d >= hO[py222.indexO(sOP)] and d >= hP[py222.indexP(sOP)]:
      dOptimal = False
      for m in range(9):
        if int(m / 3) == int(lm / 3):
          continue
        newMoves = moves[:]; newMoves.append(m)
        solved = IDAStar(py222.doMove(s, m), d - 1, newMoves, m)
        if solved and not dOptimal:
          dOptimal = True
      if dOptimal:
        return True
  return False

def stringify(moves):
  moveStr = ""
  for m in moves:
    moveStr += moveStrs[m] + " "
  return moveStr

# solve a cube state
def solveCube(s):
  solutions.clear()
  s = py222.normFC(s)
  genOTable(py222.initState(), 0)
  genPTable(py222.initState(), 0)

  # run IDA*
  solved = False
  depth = 1
  while depth <= 11 and not solved:
    solved = IDAStar(s, depth, [])
    depth += 1
  return solutions