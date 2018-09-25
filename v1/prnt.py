import gnrtr
import objs

def print_fog_maze(maze, player,tracking,treasures=[]):
    width,height=gnrtr.maze_dimensions(maze)
    block = '\u2588'

    for y in range(height):
        for x in range(width):

            is_treasure=False
            for treasure in treasures:
                if treasure.position==[y,x] and treasure.visible:
                    print("T",end="") 
                    is_treasure=True
                    break

            if [y,x]==player:
                print("X",end="")
            elif maze[y][x] in ['P','V','p'] and not is_treasure:
                if tracking and maze[y][x]=='V':
                    print("\033[91m" +"*"+"\033[00m",end="")
                else:
                    print(" ",end="")

            if maze[y][x]=='W':
                print("\033[33m" + block + "\033[37m", end="")
            elif maze[y][x]=='w':
                print(" ",end="")

        print("")


def print_enemy_maze(maze:list, player:list, enemies=[])->None:
    width,height=gnrtr.maze_dimensions(maze)
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



title = {
'm': [

' __   __ ',
'|  |_|  |',
'|       |',
'|       |',
'|       |',
'|  |_|  |',
'|_|   |_|',

    ],

'a': [

' _______ ',
'|   _   |',
'|  |_|  |',
'|       |',
'|       |',
'|   _   |',
'|__| |__|',

    ],

'z': [

' _______ ',
'|       |',
'|____   |',
' ____|  |',
'| ______|',
'| |_____ ',
'|_______|',

    ],

'e': [

' _______ ',
'|       |',
'|    ___|',
'|   |___ ',
'|    ___|',
'|   |___ ',
'|_______|',

    ]
}

def logo():
    str = 'maze'
    for row in range(len(title['m'])):
        for letter in str:
            print("\033[33m"+title[letter][row]+"\033[37m", end=' ')
        print()
