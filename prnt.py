import generator

def print_fog_maze(maze, player,tracking):
    width,height=generator.maze_dimensions(maze)
    block = '\u2588'
    for y in range(height):
        for x in range(width):
            if [y,x]==player:
                print("X",end="")
            elif maze[y][x] in ['P','V','p']:
                if tracking and maze[y][x]=='V':
                    print("\033[91m" +"*"+"\033[00m",end="")
                else:
                    print(" ",end="")
            elif maze[y][x]=='W':
                print("\033[33m" + block + "\033[37m", end="")
            elif maze[y][x]=='w':
                print(" ",end="")
        print("")


def print_enemy_maze(maze:list, player:list, enemies=[])->None:
    width,height=generator.maze_dimensions(maze)
    block = '\u2588'
    for y in range(height):
        for x in range(width):
            is_enemy=False
            if enemies!=[]:
                for i in range(len(enemies)):
                    if [y,x]==enemies[i]:
                            is_enemy=True
                            print("\033[91m" +"E"+"\033[00m",end="")
                            break
            if [y,x]==player and [y,x] not in enemies:
                print("X",end="")
            elif maze[y][x] in ['p','V'] and not is_enemy:
                print(" ",end="")
            elif maze[y][x]=='w':
                print("\033[33m" + block + "\033[37m", end="")
        print("")