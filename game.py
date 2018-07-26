import os
import getch_
import generator
import enemy_class
import prnt

def wall_check(maze, i, j):
    if maze[i][j] in ['w','W']:
        return False
    else:
        return True


def sprite_control(button_press,maze,node):
    y,x=node[0],node[1]
    maze[y][x] = "V"
    if button_press == "s":
        if wall_check(maze, y+1, x):
            y += 1
    elif button_press == "w":
        if wall_check(maze, y-1, x) and (y != 0):
            y -= 1
    elif button_press == "a":
        if wall_check(maze, y, x-1):
            x -= 1
    elif button_press == "d":
        if wall_check(maze, y, x+1):
            x += 1
    return [y,x]



def enemy_game():
    width=int(input("width?: "))
    height=int(input("height?: "))
    num_of_enemy=int(input("enemy?: "))

    os.system("clear")
    getch = getch_._Getch()

    maze,player=generator.maze_generator(width,height,True)
    enemies=[]
    enemy_class.create_enemies(maze,num_of_enemy,enemies)
    prnt.print_enemy_maze(maze,player,enemy_class.Enemy.actual_node)
    height=generator.maze_dimensions(maze,'h')

    while True:
        if player in enemy_class.Enemy.actual_node:
            print("Enemy!")
            break
        if player[0]==height-1:
            print("Winner!")
            break
        button_press = getch()
        player=sprite_control(button_press,maze,player)
        
        for enemy in enemies:
            enemy.step(maze)
        
        os.system("clear")
        prnt.print_enemy_maze(maze,player,enemy_class.Enemy.actual_node)




def fog_game():
    width=int(input("width?: "))
    height=int(input("height?: "))
    os.system("clear")
    getch = getch_._Getch()
    tracking=False

    maze,player=generator.maze_generator(width,height)

    generator.initial_visibility(maze,10)
    prnt.print_fog_maze(maze,player,tracking)
    height=generator.maze_dimensions(maze,'h')

    while True:
        if player[0]==height-1:
            print("Winner!")
            break
        button_press = getch()
        player=sprite_control(button_press,maze,player)
        generator.fog_reveal(maze,player,2)
        if button_press=='t':
            tracking=False if tracking else True
        os.system("clear")
        prnt.print_fog_maze(maze,player,tracking)


#enemy_game()
#os.system("clear")
fog_game()
