def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = None        
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = None
    return name


import random
def rpsls(player_choice):   
    player_number = name_to_number(player_choice)
    print "Player chooses", number_to_name(player_number)
       
    comp_number = random.randrange(0,5)
    print "Computer chooses", number_to_name(comp_number)
    
    if player_number == None:
        #If player_choice does not match any of the five correct input strings
        print "player_choice is wrong, please try again"
        print 
    else:
        modulo_five = (player_number - comp_number) % 5
        if (modulo_five == 1) or (modulo_five == 2):
            print "Player wins!"
        elif (modulo_five == 3) or (modulo_five == 4):
            print "Computer wins!"
        elif modulo_five == 0:
            print "Player and computer tie!"
        print

               
rpsls ("rock")
rpsls ("Spock")
rpsls ("paper")
rpsls ("lizard")
rpsls ("scissors")
rpsls ("liz")
    
    
    
