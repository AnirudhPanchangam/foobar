from itertools import chain
import collections
from collections import deque
visited = {}
def answer(src, dest):
    if src == dest:
        return 0
    moves = 0
    visited[src] = 1
    squares = deque([])
    squares.append([src])
    while squares:
        temp = []
        temp.append(all(squares.popleft()))
        squares = deque(temp)
        if dest in visited:
            return moves + 1
        moves += 1
        
def all(li):
    temp = []
    for val in li:
        temp.append(all_pos(val))
    return flatten(temp)
    
def all_pos(src):
    all_moves = [
            [1,  2],
            [1, -2],
            [-1, 2],
            [-1,-2],
            [2,  1],
            [2, -1],
            [-2, 1],
            [-2,-1]
        ]
    temp = src
    x,y = src/8, src%8
    positions = []
    for pos in all_moves:
        if is_valid_pos(x + pos[0],y + pos[1]):
            temp = src + 8*pos[0]
            temp = temp + pos[1]
            if visited.get(temp, None) == None:
                positions.append(temp)
                visited[temp] = 1
    return positions

def is_valid_pos(x, y):
    if x in range(0,8) and y in range(0,8):
        return True
    else:
        return False
def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

if __name__ == '__main__':
    print answer(43,63)
