print("Welcome to my first game!") 

playing=input("Would you like to play? ")
if playing.lower() !="yes":
    quit()
    
print("Great! let's have fun!")
score=0

answer=input("What is the sum of 7 and 9 in words? ")
if answer.lower()=="sixteen":
    print("You got it!")
    score+=1
else:
    print("Oops! you are wrong!")
    
answer=input("What is the sum of 20 and 100? ")
if answer=="120":
    print("You got it!")
    score+=1
else:
    print("Oops! you are wrong!")
    
answer=input("What is the subtraction of 700 from 1000? ")
if answer=="300":
    print("You got it!")
    score+=1
else:
    print("Oops! you are wrong!")
    
answer=input("What is the product of 30 and 30? ")
if answer=="900":
    print("You got it!")
    score+=1
else:
    print("Oops! you are wrong!")

print("You got "+str(score)+" questions correct")
print("You got "+str((score/4)*100)+"%")