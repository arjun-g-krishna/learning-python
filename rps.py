import random

def isamove(x):
    if x == 'r' or x == 'p' or x == 's' :
        return 1
    else:
        return 0

#List specifying the moves that can be made
moves = [ 'r', 'p', 's']
#Dictionary for the details of each of the moves
movealias = { 'r' : "Rock",
              'p' : "Paper",
              's' : "Scissors"
            }

#Main part of the game
ch = 'y'
huscore = 0
cpuscore = 0
scorelimit = int(input("Enter the score limit (an odd number) :")) #Set the scorelimit for the game
while cpuscore < scorelimit and huscore < scorelimit :
    humove=input("Make your move r (rock) p (paper) s (scissors):")
    if isamove(humove):
        cpumove=random.choice(moves)
        if cpumove == humove:
            print("CPU made the move " + movealias[cpumove])
            print("Tie!")
        elif cpumove == 'r' and humove == 'p':
            print("CPU made the move " + movealias[cpumove])
            print("You win this round!")
            huscore = huscore + 1
        elif cpumove == 'r' and humove == 's':
            print("CPU made the move " + movealias[cpumove])
            print("You lose this round!")
            cpuscore = cpuscore + 1
        elif cpumove == 'p' and humove == 's':
            print("CPU made the move " + movealias[cpumove])
            print("You win this round!")
            huscore = huscore + 1
        elif cpumove == 'p' and humove == 'r':
            print("CPU made the move " + movealias[cpumove])
            print("You lose this round!")
            cpuscore = cpuscore + 1
        elif cpumove == 's' and humove == 'r':
            print("CPU made the move " + movealias[cpumove])
            print("You win this round!")
            huscore = huscore + 1
        elif cpumove == 's' and humove == 'p':
            print("CPU made the move " + movealias[cpumove])
            print("You lose this round!")
            cpuscore = cpuscore + 1
        print("CPU: %d You: %d" %(cpuscore,huscore))
    else:
        print("Wrong choice!")
if cpuscore == huscore:
    print("The game ends in a tie with each scoring %d" %(cpuscore))
elif cpuscore > huscore:
    print("CPU wins the game!")
elif cpuscore < huscore:
    print("You win the game!")
print("Score CPU: %d You :%d" %(cpuscore,huscore))    
