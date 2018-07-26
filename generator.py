import random
import os

def empty_maze(width,height):
    """
    generates a 2D matrix (list of lists) with the dimensions
    given in the argument
    """
    return [['w' for x in range(width)] for y in range(height)]



def maze_dimensions(maze,dim=""):
    width=len(maze[0])
    height=len(maze)
    if dim=='w':
        return width
    if dim=='h': 
        return height
    else:
        return width,height



def maze_magnifier(maze):
    width,height=maze_dimensions(maze)
    magnified=[]

    for y in range(height):
        tmp=[]
        for x in range(width):
            for i in range(3):
                tmp.append(maze[x][y])

        for i in range(2):
            magnified.append(tmp)

    return magnified




def print_maze(maze:list, enemies=[])->None:

    width,height=maze_dimensions(maze)
    block = '\u2588'

    for y in range(height):
        for x in range(width):

            is_enemy=False
            if enemies!=[]:
                for i in range(len(enemies)):
                    if [y,x]==enemies[i]:
                            is_enemy=True
                            print("E",end="")
                            break

            if (maze[y][x]=='p') and (not is_enemy):
                print(" ",end="")
            elif maze[y][x]=='w':
                print("\033[33m" + block + "\033[37m", end="")

        print("")


def maze_initialization(maze):
    width,height=maze_dimensions(maze)
    for y in range(height):
        for x in range(width):
            if y%2==0 and x%2==0:
                maze[y][x]='1'


def available_directions(maze,node,gap,char,visited_coordinates=[]):
    width,height=maze_dimensions(maze)
    y_pos=node[0]
    x_pos=node[1]
    directions=[]

    if ((y_pos-gap>=0) and (maze[y_pos-gap][x_pos]==char) 
        and [y_pos-gap,x_pos] not in visited_coordinates):
            directions.append('up')
    
    if ((x_pos+gap<=width-1) and (maze[y_pos][x_pos+gap]==char)
        and [y_pos,x_pos+gap] not in visited_coordinates):
            directions.append('right')
    
    if ((y_pos+gap<=height-1) and (maze[y_pos+gap][x_pos]==char)
        and [y_pos+gap,x_pos] not in visited_coordinates):
            directions.append('down')

    if ((x_pos-gap>=0) and (maze[y_pos][x_pos-gap]==char)
        and [y_pos,x_pos-gap] not in visited_coordinates):
            directions.append('left')

    return directions


def random_direction(directions):
    return directions[random.randint(0,len(directions)-1)]


def set_node_to_visited(maze,node):
    y_pos=node[0]
    x_pos=node[1]
    maze[y_pos][x_pos]='p'


def next_node(node,direction,gap):
    y_pos=node[0]
    x_pos=node[1]
    if direction=='up':
        return [y_pos-gap,x_pos]
    elif direction=='right':
        return [y_pos,x_pos+gap]
    elif direction=='down':
        return [y_pos+gap,x_pos]
    elif direction=='left':
        return [y_pos,x_pos-gap]


def delete_wall(maze,node,next_node):
    wall_y=int((node[0]+next_node[0])/2)
    wall_x=int((node[1]+next_node[1])/2)
    set_node_to_visited(maze,[wall_y,wall_x])


def add_upper_boarder(maze):
    width=maze_dimensions(maze,'w')
    upper_boarder=['w' for x in range(width)]
    maze.insert(0,upper_boarder)


def add_lower_boarder(maze):
    width=maze_dimensions(maze,'w')
    lower_boarder=['w' for x in range(width)]
    maze.append(lower_boarder)


def add_left_boarder(maze):
    height=maze_dimensions(maze,'h')
    for y in range(height):
        maze[y].insert(0,'w')


def add_right_boarder(maze):
    height=maze_dimensions(maze,'h')
    for y in range(height):
        maze[y].append('w')


def add_boarders(maze):
    add_upper_boarder(maze)
    add_left_boarder(maze)
    width,height=maze_dimensions(maze)
    if width%2==0:
        add_right_boarder(maze)
    if height%2==0:
        add_lower_boarder(maze)


def start_gate(maze):
    width=maze_dimensions(maze,'w')
    for x in range(width):
        if maze[2][x]=='p':
            maze[1][x]='p'
            maze[0][x]='p'
            break
    return [0,x]

def finish_gate(maze):
    width,height=maze_dimensions(maze)
    for x in range(-1,-width-1,-1):
        if maze[height-3][x]=='p':
            maze[height-2][x]='p'
            maze[height-1][x]='p'
            break


def open_gates(maze,boarder_width=0):
    start_node=start_gate(maze)
    finish_gate(maze)
    return start_node



def maze_generator(width,height):
    nodes=[]
    maze=empty_maze(width,height)
    maze_initialization(maze)
    node=[0,0]
    set_node_to_visited(maze,node)
    nodes.append(node)
    while len(nodes)!=0:
        directions=available_directions(maze,node,2,'1')
        if directions:
            direction=random_direction(directions)
            nextnode=next_node(node,direction,2)
            set_node_to_visited(maze,nextnode)
            delete_wall(maze,node,nextnode)
            node=nextnode
            nodes.append(node)
        else:
            node=nodes.pop()
    add_boarders(maze)
    maze=maze_magnifier(maze)
    start_node=open_gates(maze)
    return maze,start_node



