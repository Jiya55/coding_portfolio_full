#path finder
'''
notes-
we'll learn-
* overide current print
*path finder algorith/breadth first search

curses- allows us to control the temirnal, color, overiede print
install curses(only windows)-pip install windows-curses

breadth first= shortes distance between start node and end mode
we are going to look in the nodes and then we will see the next node's neightbor
when we hit the end node that is the short path

we are going to use queue
first in first out datastructur, ist itme to go in will come out first
[3, 0]
remove it and process it
process it by seeing nehght bors 
check if end node
we add 3,0 to set(vsted set)
add the neight bor noded if not end
[(2,0),(3,1)]
cross, 2,0
we see below element is visted set
so we move above
[(2,0),(3,1),(1, 0)]
remove, 2,0 add to visted
continue till we reach end node
'''
import curses

from curses import wrapper
from http.client import CONTINUE
import queue
import time
maze = [

    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
'''
def main(stdscr): #standard output screen(out put of program)(we will add stuff to this)
    stdscr.clear()
    stdscr.addstr(0, 0, "hello world!")(positions, string)
    stdscr.refresh()
    stdscr.getch()#get chraracter
wrapper(main)
'''
'''
def main(stdscr): #standard output screen(out put of program)(we will add stuff to this)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    
    blue_and_black=curses.color_pair(1)
    stdscr.clear()
    stdscr.addstr(0, 0, "hello world!", blue_and_black)#d(positions, string)
    stdscr.refresh()
    stdscr.getch()#get chraracter
wrapper(main)
'''
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED= curses.color_pair(2)

    for i, row in enumerate(maze):#(index, item)
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, 'X', RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE) #to increase space we multiple j by 2

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start= 'O'
    end ='X'
    start_pos=find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited= set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors=find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c]=='#':
                continue

            new_path=path+[neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors=[]
    if row>0:#up
        neighbors.append((row-1, col))
    if row+1<len(maze):#down
        neighbors.append((row+1, col))
    if col>0:#left
        neighbors.append((row, col-1))
    if col+1<len(maze[0]):#right
        neighbors.append((row, col+1))
    return neighbors

def main(stdscr): #standard output screen(out put of program)(we will add stuff to this)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    stdscr.getch()#get chraracter
wrapper(main)
