#Globals(state) 全局变量（静态）
#Helper functions  辅助函数
#Classes(later)   类
#Define event handlers  定义事件处理程序
#create a frame   创建一个框架
#Register event handlers   注册事件处理程序
#Start frame & timers    启动框架&计时器


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    global secret_number, remaining
    secret_number = random.randrange(0, 100)
    remaining = int(math.ceil(math.log(100, 2)))
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is", remaining
   
# define event handlers for control panel
def range100():
    global secret_number, remaining
    secret_number = random.randrange(0, 100)
    remaining = int(math.ceil(math.log(100, 2)))
    print
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is", remaining
    
def range1000():
    global secret_number, remaining
    secret_number = random.randrange(0, 1000)
    remaining = int(math.ceil(math.log(1000, 2)))
    print
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is", remaining
        
def input_guess(guess):
    global remaining
    guess_number = int(guess)               
    if remaining == 0:
        print
        print "Game over"
    else:
        print
        print "Guess was", guess_number              
        remaining -= 1
        print "Number of remaining guesses is", remaining       
        if secret_number > guess_number:
            print "Higher!"
        elif secret_number < guess_number:
            print "Lower!"
        else:
            print "Correct!"

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
