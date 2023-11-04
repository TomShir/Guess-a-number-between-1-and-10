import random
from colorama import Fore 
import time 
import sys
lst = [x for x in range(1,11)]
random_num=random.choice(lst)
run_condition='True'
#changing the color of the txt  
title='Guess the number'
def colorfont():
    global color_txt 

colorfont()
color_txt=Fore.RED,Fore.BLUE,Fore.GREEN
for txt in title:
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\t{random.choice(color_txt)}{txt.upper()}')
else:
    print(Fore.RESET)
try:
        for n in range(1,11):
            print(n)
        else:
            for x in range(3):
                numerical_value=int(input('Guess a number between 1 and 10, you have 3 trys:'))
                if numerical_value==random_num:
                    time.sleep(0.2)
                    print('You have correctly guessed the number, now you will exit the loop...')
                    time.sleep(0.2)
                    sys.exit()
                else:
                    pass 
                if x==0:
                    print('Not the guessed number, you only have 2 trys left')
                elif x==1:
                    print('You now only have one try left')
                elif x==2:
                  game_over_msg='game over'
                  print(f'{Fore.RED} {game_over_msg} the correct answer was {random_num}')
                  break
except ValueError:
        pass
                
