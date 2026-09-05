import random
n = random.randint(1,10)
# For finding between 1 to 10,  4 attempts is enough statistically 
# For finding between 1 to 100,  7 attempts is enough statistically 
# For finding between 1 to 1000,  10 attempts is enough statistically 
# For finding between 1 to 10000,  13 attempts is enough statistically 
# For finding between 1 to 100000,  17 attempts is enough statistically 
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the Number: "))
    if(a>n):
        print("Guess the lower number please!")
        guesses += 1
    elif(a<n):
        print("Guess the higher number please!")
        guesses += 1

print(f"You have guess the correct number ({n}) in {guesses} attempts")
if(guesses <= 4 ):
    print("Great job boy!")
else:
    print("Better luck next time!")
    