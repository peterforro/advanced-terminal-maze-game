import enemy_class
import generator
import os



def main():
    width=int(input("width?: "))
    height=int(input("height?: "))
    num_of_enemy=int(input("enemy?: "))
    maze,start_node=generator.maze_generator(width,height)

    enemies=[]
    enemy_class.create_enemies(maze,num_of_enemy,enemies)
    generator.print_maze(maze)

    while True:
        for enemy in enemies:
            enemy.step(maze)
        os.system("clear")
        generator.print_maze(maze,enemy_class.Enemy.actual_node)
        delay=input("enter!")




if __name__ == '__main__':
    main()