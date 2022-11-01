'''GPS system'''
import curses
import queue
map= [
    ['H','0','0','0','S','0','0','0'],
    [' ','0','0','0',' ',' ','T','0'],
    [' ','G',' ','0',' ','0',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ','D'],
    ['0','0',' ','0',' ','0','0',' '],
    ['F',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ','0',' ','0','0','0','0'],
    ['I','0','B',' ','C','0','0','0']
]
landmarks = {
    'H':'home',
    'G':'grocery shop',
    'S':'school',
    'T':'theatre',
    'D':'daycare',
    'F':'friend\'s home',
    'I':'ice cream shop',
    'B':'bakery',
    'C':'cafe'

}
def print_map(map, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED= curses.color_pair(2)

    for i, row in enumerate(map):#(index, item)
        for j, value in enumerate(row):
            if (i, j) in path:
                if map[i][j]==' ':
                    stdscr.addstr(i, j*2, 'X', RED)
                else:
                    stdscr.addstr(i, j*2, map[i][j], RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)
def find_position(map, plc):
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value==plc:
                print(plc, i, j)
                return i, j
    return None
def find_neighbors(mp, row, col):
    neighbors=[]
    if row+1<len(mp):#down
        neighbors.append((row+1, col))
    if row>0:#up
        neighbors.append((row-1, col))
    if col>0:#left
        neighbors.append((row, col-1))
    if col+1<len(mp[0]):#right
        neighbors.append((row, col+1))
    return neighbors
def Path_finder(pos1, pos2, map, stdscr):
    start= find_position(map, pos1)
    endX, endY = find_position(map, pos2)
    end= map[endX][endY]

    q =  queue.Queue()
    q.put((start, [start]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        stdscr.clear()
        print_map(map, stdscr, path)
        stdscr.refresh()
        pos=map[row][col]
        if pos == end:
            stdscr.addstr(10,0, print_time(path))
            
            return path
        neighbor=find_neighbors(map,row,col)
        for coord in neighbor:
            if coord in visited:
                continue
            r, c = coord
            if map[r][c] not in [' ',start, end]:
                continue
            new_path=path+[coord]
            q.put((coord, new_path))
            visited.add(coord)


def print_time(path):
    time=len(path)*10

    if time>60:#constant for avg timeper block
        hr, min= time//60, time%60
        return f'{hr} hr(s) and {min} min(s)'

    return f'{len(path)*5} mins'

def main(stdscr): 
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    str_p= 'C'
    end_p= 'I'
    Path_finder(str_p, end_p, map, stdscr)
    stdscr.getch()
curses.wrapper(main)


