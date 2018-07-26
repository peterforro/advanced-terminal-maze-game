import os
import getch_
import gnrtr
import objs
import prnt


def wall_check(maze, i, j):
    try:
        if maze[i][j] in ['w','W']:
            return False
        else:
            return True
    except Exception:
        pass


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

    maze,sprite_pos=gnrtr.maze_generator(width,height,True)
    enemies=[]
    objs.create_objects(maze,num_of_enemy,enemies,'enemy')
    prnt.print_enemy_maze(maze,sprite_pos,objs.Enemy.actual_node)
    height=gnrtr.maze_dimensions(maze,'h')

    while True:
        button_press = getch()
        if (sprite_pos in objs.Enemy.actual_node or 
                sprite_pos[0]==height-1 or
                    button_press=='x'):
                        os.system("clear")
                        del(objs.Enemy.actual_node[:])
                        break
        sprite_pos=sprite_control(button_press,maze,sprite_pos)
        for enemy in enemies:
            enemy.step(maze)
        os.system("clear")
        prnt.print_enemy_maze(maze,sprite_pos,objs.Enemy.actual_node)




def fog_game():
    width=int(input("width?: "))
    height=int(input("height?: "))
    num_of_treasure=int(input("number of treasures?: "))
    tracking=False

    os.system("clear")
    getch = getch_._Getch()

    maze,sprite_pos=gnrtr.maze_generator(width,height)
    treasures=[]
    objs.create_objects(maze,num_of_treasure,treasures,'treasure')

    gnrtr.initial_visibility(maze,5)
    print(f"Treasures left: {objs.Treasure.num_of_treasures}\n")
    prnt.print_fog_maze(maze,sprite_pos,tracking,treasures)
    height=gnrtr.maze_dimensions(maze,'h')

    while True:
        button_press = getch()
        if (sprite_pos[0]==height-1 and 
            objs.Treasure.num_of_treasures==0 or 
                button_press=='x'):
                    os.system("clear")
                    del(objs.Treasure.position_of_treasures[:])
                    break
        if button_press=='t':
            tracking=False if tracking else True

        sprite_pos=sprite_control(button_press,maze,sprite_pos)
        gnrtr.fog_reveal(maze,sprite_pos,2)

        for treasure in treasures:
            treasure.set_visibility(maze)
            if sprite_pos==treasure.position:
                treasure.kill()
       
        os.system("clear")
        print(f"Treasures left: {objs.Treasure.num_of_treasures}\n")
        prnt.print_fog_maze(maze,sprite_pos,tracking,treasures)
