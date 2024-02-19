import random

user_win = 0
com_win = 0
draw = 0

op = ['rock','paper','scissors']

while True:
    inp = input('Type Rock,paper,scissors or quit ').lower()
    if inp == 'q':
        break
    if inp not in op:
        continue
    
    ran_num = random.randint(0,2)
    
    comp_pick = op[ran_num]
    print('computer pick', comp_pick+'.')
    
    if inp == 'rock' and comp_pick == 'scissors':
        print('You win')
        user_win += 1
    
    elif inp == 'paper' and comp_pick == 'rock':
        print('You win')
        user_win += 1
        
    elif inp == 'scissors' and comp_pick == 'paper':
        print('You win')
        user_win += 1  
    
    elif inp == comp_pick:
        print('its an draw')
        draw += 1
        
    else:
        print('you lose')
        com_win += 1

print('player win',user_win,'computer wins',com_win,'Drawss',draw)
print('goodbye!!!')