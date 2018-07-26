import generator
import random


def create_objects(maze,num_of_objects:int,object_list:list, type_of_obj:str)->None:
    if type_of_obj == "enemy":
        for i in range(num_of_objects):
            obj=Enemy(maze,i)
            object_list.append(obj)
    elif type_of_obj == "treasure":
        for i in range(num_of_objects):
            obj=Treasure(maze,i)
            object_list.append(obj)


class Enemy:
    
    num_of_enemies=0
    actual_node=[]

    def __init__(self,maze,no):
        """
        constructor of the enemy class:
        creates the object the with its instance variables
        calls the the random_position_generator() method
        """
        Enemy.num_of_enemies+=1
        self.no=no
        self.position=None
        self.visited=[] #already visited nodes
        self.path=[]    #stack!
        self.alive=True
        self.random_position_generator(maze)


    def random_position_generator(self,maze):
        width,height=generator.maze_dimensions(maze)
        while True:
            y_cor=height-int(height*0.75)
            y=random.randint(y_cor,height-1)
            x=random.randint(0,width-1)
            if (maze[y][x]=='p') and ([y,x] not in self.actual_node):
                self.position=[y,x]
                self.actual_node.append(self.position)
                self.path.append(self.position)
                break


    def death(self):
        self.alive=False
        self.position=[10000,10000]
        Enemy.num_of_enemies-=1
        self.actual_node[self.no]=self.position


    def step_forward(self,maze,directions):
        direction=generator.random_direction(directions)
        nextpos=generator.next_node(self.position,direction,1)
        self.visited.append(nextpos)
        self.position=nextpos
        self.actual_node[self.no]=self.position
        self.path.append(self.position)


    def step_back(self):
        try:
            self.position=self.path.pop()
            self.actual_node[self.no]=self.position
        except Exception:
            self.actual_node[self.no]=[10000,1000]
            Enemy.num_of_enemies-=1
            pass


    def step(self,maze):
        if self.position[0]==0:
            self.death()
        if self.alive:
            directions=generator.available_directions(maze,self.position,1,'p',self.visited)
            if directions!=[]:
                self.step_forward(maze,directions) 
            else:
                self.step_back()


class Treasure:

    position_of_treasures=[]
    num_of_treasures=0

    def __init__(self,maze,no):
    """
    constructor of the enemy class:
    creates the object the with its instance variables
    calls the the random_position_generator() method
    """
    Treasure.num_of_treasures+=1
    self.no=no
    self.position=None
    self.random_position_generator(maze)

    def random_position_generator(self,maze):
        width,height=generator.maze_dimensions(maze)
        while True:
            y=random.randint(0,height-1)
            x=random.randint(0,width-1)
            if (maze[y][x]=='p') and ([y,x] not in self.position_of_treasures):
                self.position=[y,x]
                self.position_of_treasures.append(self.position)
                break

    def kill(self):
        position_of_treasures[no] = [10000,10000]
        Treasure.num_of_treasures-=1