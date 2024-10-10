import random

class botPlayer:
    #set life and strength
    def __init__(self):
        self.lifePoints = 100
        self.strength = 0

    #set strength for each player
    def setStrength(self):
        self.strength = random.randrange(5, 55, 5)
    
    #subtract lifepoints
    def receiveDamage(self, incomingdamage):
        self.lifePoints -= incomingdamage
    
class Battle:
    print("Bot Battle!")

    p1 = botPlayer()
    p2 = botPlayer()
    turn = 2
    quit = 'h'

    while quit.lower() == 'h':
        #Player's Turn
        print("Bot1 life points:", p1.lifePoints)
        print("Bot2 Life Points:", p2.lifePoints)

        #Alternate turns
        if turn % 2 == 0:
            print("Bot1 Your Turn!")
        
        else:
            print("Bot2 Your Turn!")

        quit = input("Press h to hit, q to quit: ")
        print()

        #Report Winner
        if quit.lower() != 'h' or p1.lifePoints < 1 or p2.lifePoints < 1:
            print("Nice battle!")

            #winner TBD
            if p1.lifePoints > p2.lifePoints:
                winner = 'Bot1'
            if p1.lifePoints < p2.lifePoints:
                winner = 'Bot2'

            print( winner, "wins this round!")
            print("Thanks for playing!")
            break

        p1.setStrength()
        p2.setStrength()

        #determine damage from strength of each bot
        if p1.strength > p2.strength:
            damage = p1.strength - p2.strength
            loser = 'Bot2'
            p2.receiveDamage(damage)

        elif p1.strength < p2.strength:
            damage = p2.strength - p1.strength
            loser = 'Bot1'
            p1.receiveDamage(damage)

        elif p1.strength == p2.strength:
            damage = 0
            loser = 'Nobody'

        #report strength and damage
        print("Bot1 strength:", p1.strength, ", Bot 2 strength:", p2.strength, '.', loser, 'you have', damage, 'points of damage.')
        turn += 1
        

#Main Program
Battle()



