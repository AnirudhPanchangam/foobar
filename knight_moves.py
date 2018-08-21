from itertools import chain
import collections
visited = {}
def answer(src, dest):
    if src == dest:
        return 0
    moves = 0
    visited[src] = 1
    squares = []
    squares.append(src)
    while squares:
        moves = moves +1
        temp = []
        for val in squares:
            temp.append(all_pos(val))
        squares = flatten(temp)
        if dest in visited:
            global visited
            visited = {}            
            return moves
    
        
    
    
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
