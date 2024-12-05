import random

print("welcome to the guessing game")
print("Enter your guess between 0 to 10")


number = random.randint(0,10)
print("Guess a number between 0 and 10.")
    
  

while True:
    
    guess = int(input("Enter your guess: "))
        
    if guess == number:
        print("That is the correct number.")
        
    else:
        print("Ooops, that is the wrong number. {0} is the correct guess".format(number))
        break
    