import os
import game
import prnt


def menu():
    while True:
        os.system("clear")
        prnt.logo()
        print("\n"*2+"1.\tEnemy Game\n2.\tTreasure Hunt\n3.\tExit")
        select=int(input("\nselection?: "))
        if select==1:
            os.system("clear")
            game.enemy_game()
        elif select==2:
            os.system("clear")
            game.fog_game()
        elif select==3:
            exit()
            
       
def main():
    menu()

if __name__ == '__main__':
    main()