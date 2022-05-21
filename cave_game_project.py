
import random
import os



def map_symbols(symbol):
    if symbol == 0:
        return ' '
    if symbol == -1:
        return 'X'
    if symbol == 1:
        return 'P'
    if symbol == 2 or symbol == 4:
        return 'M'
    if symbol == 3:
        return 'T'
    

def display_map(a_map):
    os.system('clear')
    print('+' + '-'*10 + '+')
    for line in a_map:
        print('|' + ''.join(map_symbols(symbol) for symbol in line) + '|')
    print('+' + '-'*10 + '+')


base_map = [[0 for _ in range(10)] for _ in range(10)]

def generate_map():
    num_monster= int(input("how many monsters do you want?(1 or 2)"))
    #print("Base map:")
    #display_map(base_map)
    
    for _ in range(10):
        obstacle_x = random.randint(0,9)
        obstacle_y = random.randint(0,9)
        base_map[obstacle_x][obstacle_y] = -1
    #print("Map with obstacles:")   
    #display_map(base_map)
    
    player_positioned = False
    while not player_positioned:
        player_x = random.randint(0,9)
        player_y = random.randint(0,9)
        player_positioned = (base_map[player_x][player_y] != -1)
    base_map[player_x][player_y] = 1
    #print("Map with obstacles and player:")   
    #display_map(base_map)
    monster_positioned = False
    while not monster_positioned:
        monster_x = random.randint(0,9)
        monster_y = random.randint(0,9)
        if (abs(player_x - monster_x) + abs(player_y - monster_y) > 4) and (base_map[monster_x][monster_y] != -1):
            base_map[monster_x][monster_y] = 2
            #print("monster 1")
            monster_positioned=True
        else:
            continue
        #print("Map with obstacles, player and a monster:")   
        #display_map(base_map)
   
    if num_monster==2:
        monster_positioned2 = False
        while not monster_positioned2:
            monster2_x = random.randint(0,9)
            monster2_y = random.randint(0,9)
            if (abs(player_x - monster2_x) + abs(player_y - monster2_y) > 4) and (base_map[monster2_x][monster2_y] != -1) and (base_map[monster2_x][monster2_y] != 2):

                base_map[monster2_x][monster2_y] = 4
                #print("monster 2")
                monster_positioned2=True
            else:
                continue
    else:
        pass


    treasure_positioned = False
    while not treasure_positioned:
        t_x = random.randint(0,9)
        t_y = random.randint(0,9)
        treasure_positioned = (abs(player_x - t_x) + abs(player_y - t_y) > 4) and (base_map[t_x][t_y] != -1) and (abs(monster_x - t_x) + abs(monster_y - t_y) > 4) and (abs(monster2_x - t_x) + abs(monster2_y - t_y) > 4)
    base_map[t_x][t_y] = 3
   # print("completed map:")
    display_map(base_map)

    return base_map

generate_map()



def find_monster():
    for a in range(10):
        for b in range(10):
            if base_map[a][b]==2:
                
                return a, b
monster_x, monster_y= find_monster()

def find_monster2():
    
    for a in range(10):
        for b in range(10):
            if base_map[a][b]==4:
                
                return a, b


monster2_x,monster2_y=find_monster2()
#print(monster_x, monster_y)

def move_monster():
    global monster_x
    global monster_y
    monster_moved=False

    while monster_moved==False:
        num=random.randint(0,3)
        if num==0:         #up
            if monster_x>0 and (base_map[monster_x-1][monster_y] != -1) and (base_map[monster_x-1][monster_y] != 3):
                base_map[monster_x][monster_y]=0
                monster_x -=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1

        elif num==1:         #right
            if monster_y<9 and (base_map[monster_x][monster_y+1] != -1) and (base_map[monster_x][monster_y+1] != 3):
                base_map[monster_x][monster_y]=0
                monster_y +=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1
        if num==2:         #down 
            if monster_x<9 and (base_map[monster_x+1][monster_y] != -1) and (base_map[monster_x+1][monster_y] != 3):
                base_map[monster_x][monster_y]=0
                monster_x +=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1
        elif num==3:         #left
            if monster_y>0 and (base_map[monster_x][monster_y-1] != -1) and (base_map[monster_x][monster_y-1] != 3):
                base_map[monster_x][monster_y]=0
                monster_y -=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1

def move_monster2():
    global monster2_x
    global monster2_y
    monster_moved=False

    while monster_moved==False:
        num=random.randint(0,3)
        if num==0:         #up
            if monster2_x>0 and (base_map[monster2_x-1][monster2_y] != -1) and (base_map[monster2_x-1][monster2_y] != 3) and (base_map[monster2_x-1][monster2_y] != 2):
                base_map[monster2_x][monster2_y]=0
                monster2_x -=1
                base_map[monster2_x][monster2_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1

        elif num==1:         #right
            if monster2_y<9 and (base_map[monster2_x][monster2_y+1] != -1) and (base_map[monster2_x][monster2_y+1] != 3) and (base_map[monster2_x][monster2_y +1] != 2):
                base_map[monster2_x][monster2_y]=0
                monster2_y +=1
                base_map[monster2_x][monster2_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1
        if num==2:         #down 
            if monster2_x<9 and (base_map[monster2_x+1][monster2_y] != -1) and (base_map[monster2_x+1][monster2_y] != 3) and (base_map[monster2_x+1][monster2_y] != 2):
                base_map[monster2_x][monster2_y]=0
                monster2_x +=1
                base_map[monster2_x][monster2_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1
        elif num==3:         #left
            if monster_y>0 and (base_map[monster2_x][monster2_y-1] != -1) and (base_map[monster2_x][monster2_y-1] != 3) and (base_map[monster2_x][monster2_y-1] != 2):
                base_map[monster2_x][monster2_y]=0
                monster2_y -=1
                base_map[monster2_x][monster2_y]=2
                monster_moved=True
                if base_map[player_x][player_y]==0:
                    base_map[player_x][player_y]==1
                
    


def find_player():
    
    for i in range(10):
        for j in range(10):
            if base_map[i][j]==1:
                
                return i, j


player_x, player_y = find_player()
#print(player_x)
#print(player_y)


def move_right():
    global player_x
    global player_y
    if (player_y < 9) and (base_map[player_x ][player_y+1] != -1):
        base_map[player_x][player_y]=0
        player_y += 1
        base_map[player_x][player_y]=1
        move_monster()
        move_monster2()
#        if base_map[player_x][player_y]==2:
            #print("you lost")
   #         return True
  #      else:
    #        return False
    else:
        print("you cant move here, try again ")
    return 

def move_left():
    global player_x
    global player_y
    if (player_y> 0) and (base_map[player_x][player_y -1] != -1):
        base_map[player_x][player_y]=0
        player_y -= 1
        base_map[player_x][player_y]=1
        move_monster()
        move_monster2()
     #   if base_map[player_x][player_y]==2:
            #print("you lost")
     #       return True
    #    else:
     #       return False
       
    else:
        print("you cant move here, try again ")
    return 

def move_down():
    global player_x
    global player_y
    if (player_x<9) and (base_map[player_x +1][player_y] != -1):
        base_map[player_x][player_y]=0
        player_x += 1
        base_map[player_x][player_y]=1
        move_monster()
        move_monster2()
      #  if base_map[player_x][player_y]==2:
            #print("you lost")
     #       return True
     #   else:
      #      return False
       
    else:
        print("you cant move here, try again ")
    return 

def move_up():
    global player_x
    global player_y
    if (player_x> 0) and (base_map[player_x -1][player_y] != -1):
        base_map[player_x][player_y]=0
        player_x -= 1
        base_map[player_x][player_y]=1
        move_monster()
        move_monster2()
  #      if base_map[player_x][player_y]==2:
            #print("you lost")
  #          return True
  #      else:
   #         return False
    else:
        print("you cant move here, try again ")
    return 



def find_treasure():
    for k in range(10):
        for l in range(10):
            if base_map[k][l]==3:
                
                return k, l

t_x, t_y=find_treasure()


def moving():
    again=True
    while again==True:
        #move_monster()
        move=input("where would you like to move?(w,a,s,d)")
        
        if move=="a":
            #move_left()
            
            if base_map[player_x][player_y-1]==3:
                print("you win, good job!")
                again=False
                return
            elif base_map[player_x][player_y-1]==2:
                print("you lost :/")
                again=False 
                return
            else:
                move_left()
                if base_map[monster_x][monster_y]==base_map[player_x][player_y] or base_map[monster2_x][monster2_y]==base_map[player_x][player_y]:
                    print("you lost")
                    again=False
                    return

        elif move=="d":
            #move_right()
            if base_map[player_x][player_y+1]==3:
                print("you win, good job!")
                again=False
                return
            elif base_map[player_x][player_y+1]==2:
                print("you lost :/")
                again=False 
                return
            else:
                move_right()
                if base_map[monster_x][monster_y]==base_map[player_x][player_y] or base_map[monster2_x][monster2_y]==base_map[player_x][player_y]:
                    print("you lost")
                    again=False
                    return

        elif move=="w":
            
            if base_map[player_x-1][player_y]==3:
                print("you win, good job!")
                again=False
                return
            elif base_map[player_x-1][player_y]==2:
                print("you lost :/")
                again=False 
                return
            else:
                move_up()
                if base_map[monster_x][monster_y]==base_map[player_x][player_y] or base_map[monster2_x][monster2_y]==base_map[player_x][player_y]:
                    print("you lost")
                    again=False
                    return
        elif move=="s":
            #move_down()
            if base_map[player_x+1][player_y]==3:
                print("you win, good job!")
                again=False
                return
            elif base_map[player_x+1][player_y]==2:
                print("you lost :/")
                again=False 
                return
            else:
                move_down()
                if base_map[monster_x][monster_y]==base_map[player_x][player_y] or base_map[monster2_x][monster2_y]==base_map[player_x][player_y]:
                    print("you lost")
                    again=False
                    return
        else:
            print("wrong input")
        
            

        display_map(base_map)
    return 


moving()

