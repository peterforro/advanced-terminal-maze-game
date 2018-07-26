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


def print_maze(maze):
    width,height=maze_dimensions(maze)
    for y in range(height):
        for x in range(width):
            print(maze[y][x],end="")
        print("")



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




maze=[[1,2,3],[4,5,6],[7,8,9]]
maze=maze_magnifier(maze)


print_maze(maze)
    
    

