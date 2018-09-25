import random
import os


def custom_size_empty_matrix(width,height):
    """
    Do: Generates a custom size matrix, initialized with zeros
    Args: width and height of the matrix
    Return: Custom matrix (list of lists) filled with 0s.
    """
    return [[" " for x in range(width)] for y in range(height)]



def print_matrix(matrix,height):
    """
    Do: Prints the matrix (raw form of the maze) to the standard output
    Args: the matrix and its height
    Return: None
    """
    convert_to_str = lambda elem: str(elem)
    tmp = ""
    for y in range(height):
        tmp += " ".join(map(convert_to_str, matrix[y])) + "\n"
    print(tmp)



def initialize_matrix(matrix,width,height):
    """
    Do: initializes the matrix for the maze generator procedure.
    Actually it makes a graph from the matrix
    cells with 1 are representing the nodes of the graph. 0s are the walls of the labirynth.
    Every node is surrounded by walls (0s)
    The DFS algorithm makes a random circleless tree graph from the nodes.
    Args: matrix and its dimensions
    Return: None
    """
    for y in range(height):
        for x in range(width):
            if y % 2 == 0 and x % 2 == 0:
                matrix[y][x] = 0



def available_directions(matrix,width,height,position):
    """
    Do: examines the sorrounding of the actual node (given with the position).
    Makes a list from the possible directions, where the program can proceed the maze
    generation.
    Args: matrix and its dimensions, coordinates of the actual position (tuple)
    Return: List of the directions
    """
    y_pos,x_pos=position
    directions = []
    if y_pos - 2 >= 0 and matrix[y_pos-2][x_pos] == 0:
        directions.append("N")
    if y_pos + 2 <= height-1 and matrix[y_pos+2][x_pos] == 0:
        directions.append("S")
    if x_pos - 2 >= 0 and matrix[y_pos][x_pos-2] == 0:
        directions.append("W")
    if x_pos + 2 <= width-1 and matrix[y_pos][x_pos+2] == 0:
        directions.append("E") 
    return directions



def choose_random_direction(directions):
    """
    Do: randomly chooses a direction from the list given as an argument
    Arg: list of strings
    Return: a string
    """
    return random.choice(directions)



def set_node_to_visited(matrix,position):
    """
    Do: sets the value of the visited node (given as position in the arguments) to 1
    Arg: matrix, the visited node's position
    Return: None 
    """
    y_pos, x_pos = position
    matrix[y_pos][x_pos] = 1



def define_next_position(position,direction):
    """
    Do: Defines the coordinates of the next position, based on the actual
    position, and the randomly choosed direction
    Arg: the coordinates of the actual position, direction
    Return: coordinates of the next position
    """
    y_pos,x_pos = position
    if direction == "N":
        y_pos -= 2
    elif direction == "S":
        y_pos += 2
    elif direction == "E":
        x_pos += 2
    elif direction == "W":
        x_pos -= 2
    return y_pos,x_pos



def make_a_path(matrix,position,next_position):
    """
    Do: makes a path between the actual and the next position
    (extends the maze between the two nodes)
    Arg: matrix, coordinates of the actual and the next positions
    Return: None
    """
    y_pos,x_pos = position
    y_next,x_next = next_position
    wall_y = (y_pos + y_next)//2
    wall_x = (x_pos + x_next)//2
    set_node_to_visited(matrix,(wall_y,wall_x))


    
def random_maze_generator(width,height):
    """
    Do: generates the custom size random maze,
    based on the DFS (depth-first-search) maths algorithm
    by executing the small steps of the procedure
    Arg: the width and the height of the desired maze
    Return: random maze (matrix)
    """
    os.system("cls")
    matrix = custom_size_empty_matrix(width,height)
    initialize_matrix(matrix,width,height)
    position = 0,0
    node_stack = [position]
    os.system("cls")
    print_matrix(matrix,height)
    input("-ENTER-")
    os.system("cls")
    while node_stack != []:
        set_node_to_visited(matrix,position)
        directions = available_directions(matrix,width,height,position)
        if directions:
            direction = choose_random_direction(directions)
            next_position = define_next_position(position,direction)
            make_a_path(matrix,position,next_position)
            position = next_position
            node_stack.append(position)
        else:
            position = node_stack.pop()
        print_matrix(matrix,height)
        input("-ENTER-")
        os.system("cls")
    return matrix





#---------------------------------------TESTING-----------------------------------------
#---------------------------------------------------------------------------------------
def main():
    width = int(input("width?: "))
    height = int(input("height?: "))
    random_maze_generator(width,height)
    


if __name__ == '__main__':
    main()