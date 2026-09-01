import random

def game():
    print("Starting the Game...")
    score = random.randint(1,100)
    print(f"Your Score {score}")

    #fetch pervious score from hi-score.txt
    with open("hi-score.txt") as h:
        hi_score = h.read()
        if hi_score != "":
            hi_score = int(hi_score)
        else:
            hi_score = 0
    #comparing score and high score 
    with open("hi-score.txt","w") as h:
        if (score>hi_score):
            h.write(str(score))


game()