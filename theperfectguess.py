import random
num = random.randint(0,100)
count = 0 
def theperfectguess():
    global count
    n = int(input("Guess the Number(btw 0 to 100) : "))   
    if n>num:
        print("Lower number Please")
        count+=1
        theperfectguess()
    elif n<num:
        print("higher number Please")
        count+=1
        theperfectguess()
    elif n == num:
        count+=1
        print(f"You haved Guessed the number {num} correctly in {count} attempts")
        return

theperfectguess()