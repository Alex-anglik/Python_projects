import random
import os 


#blank_map=[]
#lines=[]
#for i in range(10):
#    lines.append(0)
#for x in range(10):
 #   blank_map.append(lines)
#print(blank_map)

def map_symbols(symbol):
    if symbol == 0:
        return ' '
    if symbol == -1:
        return 'X'
    if symbol == 1:
        return 'P'
    if symbol == 2:
        return 'M'
    if symbol == 3:
        return 'T'
    

def display_map(a_map):
    print('+' + '-'*10 + '+')
    for line in a_map:
        print('|' + ''.join(map_symbols(symbol) for symbol in line) + '|')
    print('+' + '-'*10 + '+')


base_map = [[0 for _ in range(10)] for _ in range(10)]

def generate_map():
    
    print("Base map:")
    display_map(base_map)
    
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
        monster_positioned = (abs(player_x - monster_x) + abs(player_y - monster_y) > 4) and (base_map[monster_x][monster_y] != -1) 
    base_map[monster_x][monster_y] = 2
    #print("Map with obstacles, player and a monster:")   
    #display_map(base_map)

    treasure_positioned = False
    while not treasure_positioned:
        t_x = random.randint(0,9)
        t_y = random.randint(0,9)
        treasure_positioned = (abs(player_x - t_x) + abs(player_y - t_y) > 4) and (base_map[t_x][t_y] != -1) and (abs(monster_x - t_x) + abs(monster_y - t_y) > 4)
    base_map[t_x][t_y] = 3
    print("completed map:")
    display_map(base_map)

    return base_map

generate_map()



def find_monster():
    
    for a in range(10):
        for b in range(10):
            if base_map[a][b]==2:
                
                return a, b

monster_x, monster_y= find_monster()
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
        elif num==1:         #right
            if monster_y<9 and (base_map[monster_x][monster_y+1] != -1) and (base_map[monster_x][monster_y+1] != 3):
                base_map[monster_x][monster_y]=0
                monster_y +=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
        if num==2:         #down 
            if monster_x<9 and (base_map[monster_x+1][monster_y] != -1) and (base_map[monster_x+1][monster_y] != 3):
                base_map[monster_x][monster_y]=0
                monster_x +=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
        elif num==3:         #left
            if monster_y>0 and (base_map[monster_x][monster_y-1] != -1) and (base_map[monster_x][monster_y-1] != 3):
                base_map[monster_x][monster_y]=0
                monster_y -=1
                base_map[monster_x][monster_y]=2
                monster_moved=True
    


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
        #print(player_x)
        #print(player_y)
        #if base_map[t_x][t_y]==1:
        #    print("you win!!!")
         #   return False
        #else:
        #    return True
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
        #if base_map[t_x][t_y]==1:
        #    print("you win!!!")
        #    return False
        #else:
         #   return True
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
        #if base_map[t_x][t_y]==1:
         #   print("you win!!!")
         #  return False
        #else:
         #  return True
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
        #if base_map[t_x][t_y]==1:
          #  print("you win!!!")
            #return False
        #else:
         #   return True 
    else:
        print("you cant move here, try again ")
    return 

#def outcome():
 #   global t_x, t_y
#    if base_map[t_x][t_y]==1:
        
  #      return False
    #elif base_map[player_x][player_y]==3:
     #   print("You win!!! good job")
     #   return False
 #   else:
  #      return True

def find_treasure():
    for k in range(10):
        for l in range(10):
            if base_map[k][l]==1:
                
                return k, l

t_x, t_y=find_treasure()


def moving():
    again=True
    while again==True:
        move_monster()
        move=input("where would you like to move?(w,a,s,d)")
        
        if move=="a":
            move_left()
            #temp=outcome()
            #if temp==False:
            #    print("you win!!!")
           #     again=False

        elif move=="d":
            move_right()
            #temp=outcome()
            #if temp==False:
            #    print("you win!!!")
           #    again=False
        elif move=="w":
            move_up()
           # temp=outcome()
           # if temp==False:
           #     print("you win!!!")
           #     again=False
        elif move=="s":
            move_down()
            #temp=outcome()
            #if temp==False:
           #     print("you win!!!")
            #    again=False
        else:
            print("wrong input")
        
            

        display_map(base_map)
        
    return 


moving()

