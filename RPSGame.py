from random import randint

#create a list of play options || three shapes with an outstretched hand
shape = ["Rock","Paper", "Scissors"]


#a random play is assigned to computer
computer = shape[randint(0,2)]

#initialize player to False
player = False


while player == False:

    player = input("Rock, Paper, Scissors?")
    
    # player and computer has assigned same shapes
    if player == computer:
        print("Its a tie !!!!")
    
    # Paper covers Rock and Rock smashes Scissors     
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes",computer)
            
    # Scissors cut Paper and Paper covers Rock       
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    
    # Rock smashes Scissors and Scissors cut  Paper       
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win", player, "cut", computer)
            
    else:
        print("Please select right choices!!! Good Luck :) ")
        
        
    #to continue the loop
    player = False
    computer = shape[randint(0,2)]