#################################################################################
##                                                                             ##
##                           JUST FOR DEMONSTRATION                            ##
##                            NOT THE ACTUAL CODE!                             ##
##                                                                             ##
#################################################################################


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


def print_maze(maze:list,node,nextnode=[-10,-10])->None:

    width,height=maze_dimensions(maze)
    block = '\u2588'

    for y in range(height):
        for x in range(width):
            if [y,x] == node:
                print("\033[91m" + block + "\033[00m", end="")
            elif [y,x] == nextnode:
                print("\033[92m" + block + "\033[00m", end="")
            elif maze[y][x] in ['1','p']:
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
    return maze


def available_directions(maze,node,gap,char,visited_coordinates):
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
    return maze


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
    maze=set_node_to_visited(maze,[wall_y,wall_x])
    return maze


def add_upper_boarder(maze):
    width=maze_dimensions(maze,'w')
    upper_boarder=['w' for x in range(width)]
    maze.insert(0,upper_boarder)
    return maze


def add_lower_boarder(maze):
    width=maze_dimensions(maze,'w')
    lower_boarder=['w' for x in range(width)]
    maze.append(lower_boarder)
    return maze


def add_left_boarder(maze):
    height=maze_dimensions(maze,'h')
    for y in range(height):
        maze[y].insert(0,'w')
    return maze


def add_right_boarder(maze):
    height=maze_dimensions(maze,'h')
    for y in range(height):
        maze[y].append('w')
    return maze


def add_boarders(maze,node):
    maze=add_upper_boarder(maze)
    delay(maze,node)
    maze=add_left_boarder(maze)
    delay(maze,node)
    width,height=maze_dimensions(maze)
    if width%2==0:
        maze=add_right_boarder(maze)
        delay(maze,node)
    if height%2==0:
        maze=add_lower_boarder(maze)
        delay(maze,node)
    return maze


def open_gates(maze,start,node):
    start_y=start[0]
    start_x=start[1]+1
    maze[start_y][start_x]='p'

    delay(maze,node)

    width,height=maze_dimensions(maze)
    finish_x=None
    for x in range(-1,-width-1,-1):
        if maze[height-2][x]=='p':
            finish_x=x
            break
    finish_y=height-1
    maze[finish_y][finish_x]='p'

    delay(maze,node)

    finish_x+=width
    return maze,[start_y,start_x],[finish_y,finish_x]

def delay(maze,node,nextnode=[-10,-10]):
    enter=input("Press enter")
    os.system("clear")
    print_maze(maze,node,nextnode)

def maze_generator(width,height):
    nodes=[]
    maze=empty_maze(width,height)

    delay(maze,[])

    maze=maze_initialization(maze)

    delay(maze,[])

    node=start=[0,0]

    delay(maze,node)

    maze=set_node_to_visited(maze,node)
    nodes.append(node)

    while len(nodes)!=0:
        delay(maze,node)
        directions=available_directions(maze,node,2,'1',[])
        if directions:
            direction=random_direction(directions)
            nextnode=next_node(node,direction,2)
            delay(maze,node,nextnode)
            maze=set_node_to_visited(maze,nextnode)
            maze=delete_wall(maze,node,nextnode)
            node=nextnode
            nodes.append(node)
        else:
            node=nodes.pop()
        

    maze=add_boarders(maze,node)
    maze,start_pos,finish_pos=open_gates(maze,start,node)
    return maze,start_pos,finish_pos




#----------------------TEST-------------------------
width=int(input("width?: "))
height=int(input("height?: "))

maze,start_pos,finish_pos=maze_generator(width,height)
