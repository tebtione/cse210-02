'''
Connor Baltich
Hilo
'''

# Don't get mad I use random libraies
# Its way better than doing the math and using the built in random
import random

def main():
    gameLoop()

def gameLoop():
    # Game variables
    currentCard = random.randint(1, 13)
    gameLoop = True
    score = 300
    
    while (gameLoop):
        inp = input(f"The card is {currentCard}, 'h' or 'l': ")

        if (score <= 0):
            print("Game Over!")
        else:
            # Create next card
            newCard = random.randint(1, 13)

            # If win
            if ((inp == 'l' and newCard < currentCard) or (inp == 'h' and newCard > currentCard)):
                currentCard = newCard
                score += 100
                print(f"Great guess! The card was {newCard}. Your score is now {score}.")

            # Loose    
            else:
                score -= 70
                print(f"Rough guess... The card was {newCard}. Your score is now {score}.")
    
            # Prompt for game to continue
            gameLoop = playAgain()

def playAgain():
    return (input("Keep playing? ") == 'y')

if __name__ == "__main__":
    main()