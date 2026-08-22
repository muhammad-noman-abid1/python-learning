import random
def game():
    print("You are playing a Game... ")
    score = random.randint(10,50) # to take the random hiscore
    with open("hiscore.txt") as f: # open the file hiscore.txt
        hiscore = f.read() # reads the file
        if(hiscore!=""):  # condition is that if hi score is not equal to blank then
            hiscore = int(hiscore)   #  take the hiscore
        else:  # if file is eqaul to blank then 
            hiscore = 0   #  consider hiscore is zero

    print(f"Your score: {score}")  # prints the current score 
    if(score>hiscore):  # condition is if current score is higher than the score in hiscore.txt then 
        with open ("hiscore.txt", "w") as f:   # open the file
            f.write( str(score))  # write the new high score if its grater thtan previous score
        return score

game()