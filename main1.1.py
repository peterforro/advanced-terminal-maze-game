import random
import os

def empty_maze(width,height):
    """
    generates a 2D matrix (list of lists) with the dimensions
    given int the argument
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


def print_maze(maze:list, enemies:list)->None:
    width,height=maze_dimensions(maze)
    block = '\u2588'
    for y in range(height):
        for x in range(width):
            for i in range(len(enemies)):
                if [y,x]==enemies[i]:
                        print("E",end="")
                        break
            if (maze[y][x]=='p') and ([y,x]!=enemies[i]):
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
            directions.append(1)
    
    if ((x_pos+gap<=width-1) and (maze[y_pos][x_pos+gap]==char)
        and [y_pos,x_pos+gap] not in visited_coordinates):
            directions.append(2)
    
    if ((y_pos+gap<=height-1) and (maze[y_pos+gap][x_pos]==char)
        and [y_pos+gap,x_pos] not in visited_coordinates):
            directions.append(3)

    if ((x_pos-gap>=0) and (maze[y_pos][x_pos-gap]==char)
        and [y_pos,x_pos-gap] not in visited_coordinates):
            directions.append(4)

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
    if direction==1:
        return [y_pos-gap,x_pos]
    elif direction==2:
        return [y_pos,x_pos+gap]
    elif direction==3:
        return [y_pos+gap,x_pos]
    elif direction==4:
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


def add_boarders(maze):
    maze=add_upper_boarder(maze)
    maze=add_left_boarder(maze)
    width,height=maze_dimensions(maze)
    if width%2==0:
        maze=add_right_boarder(maze)
    if height%2==0:
        maze=add_lower_boarder(maze)
    return maze


def open_gates(maze,start):
    start_y=start[0]
    start_x=start[1]+1
    maze[start_y][start_x]='p'
    width,height=maze_dimensions(maze)
    finish_x=None
    for x in range(-1,-width-1,-1):
        if maze[height-2][x]=='p':
            finish_x=x
            break
    finish_y=height-1
    maze[finish_y][finish_x]='p'
    finish_x+=width
    return maze,[start_y,start_x],[finish_y,finish_x]


def maze_generator(width,height):
    nodes=[]
    maze=empty_maze(width,height)
    maze=maze_initialization(maze)
    node=start=[0,0]
    maze=set_node_to_visited(maze,node)
    nodes.append(node)
    while len(nodes)!=0:
        directions=available_directions(maze,node,2,'1',[])
        if directions:
            direction=random_direction(directions)
            nextnode=next_node(node,direction,2)
            maze=set_node_to_visited(maze,nextnode)
            maze=delete_wall(maze,node,nextnode)
            node=nextnode
            nodes.append(node)
        else:
            node=nodes.pop()
    maze=add_boarders(maze)
    maze,start_pos,finish_pos=open_gates(maze,start)
    return maze,start_pos,finish_pos



class Enemy:
    
    enemy_actual_coordinates=[]

    def __init__(self,maze,no):
        """
        constructor of the enemy class:
        creates the object the with its variables
        it puts the enemy obj to a random position
        it puts the actual coordinates to the enemy_coordinates list
        """
        self.no=no
        self.position=None
        self.visited=[] #already visited nodes
        self.path=[]    #stack!
        self.alive=True
        width,height=maze_dimensions(maze)
        while True:
            y=random.randint(0,height-1)
            x=random.randint(0,width-1)
            if (maze[y][x]=='p') and ([y,x] not in self.enemy_actual_coordinates):
                self.position=[y,x]
                self.enemy_actual_coordinates.append(self.position)
                break

    def step(self,maze,finish_pos):
        if self.position==finish_pos:
            self.alive=False
            self.position=[10000,10000]
            self.enemy_actual_coordinates[self.no]=self.position
        if self.alive:
            directions=available_directions(maze,self.position,1,'p',self.visited)
            if directions!=[]: 
                direction=random_direction(directions)
                nextpos=next_node(self.position,direction,1)
                self.visited.append(nextpos)
                self.position=nextpos
                self.enemy_actual_coordinates[self.no]=self.position
                self.path.append(self.position)
            else:
                self.position=self.path.pop()
                self.enemy_actual_coordinates[self.no]=self.position
            
        
def create_enemy(maze,num_of_enemy:int,enemies:list)->None:
    for i in range(num_of_enemy):
        enemy=Enemy(maze,i)
        enemies.append(enemy)


#----------------------TEST-------------------------
width=int(input("width?: "))
height=int(input("height?: "))
num_of_enemy=int(input("enemy?: "))
maze,start_pos,finish_pos=maze_generator(width,height)

enemies=[]
create_enemy(maze,num_of_enemy,enemies)
while True:
    for enemy in enemies:
        enemy.step(maze,finish_pos)
    os.system("clear")
    print_maze(maze,Enemy.enemy_actual_coordinates)
    delay=input("enter!")
