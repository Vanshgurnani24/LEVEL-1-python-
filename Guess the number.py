import random
low_value=1 #lowest value
high_value=10000 #highest value
MaxAttempts=10 #maximum attempts for a user
random_number=random.randint(low_value,high_value) #generates a random number between low and high value



def get_guess():    #Function that will take input from user
    while True:
        try:
            guess=int(input(f"Guess a number between {low_value} and {high_value}: "))
            if low_value<=guess<=high_value:
                return guess
            else:
                print("Error, pls print a number within specified range.......")
        except ValueError:
            print("Invalid input. Pls enter a valid input")
def check_guess(guess,random_number):
    if guess==random_number:
        return "Correct"
    elif guess<random_number:
        return "Too Low"
    else:
        return "Too High"
def PlayTheGame():
    attempts=0
    won=False
    while attempts<MaxAttempts:
        attempts+=1
        guess=get_guess()
        result=check_guess(guess,random_number)

        if result=="Correct":
            print("Congratulation. You guessed the secret number ",random_number," in ",attempts," attempts")
            won=True
            break
        else:
            print(result," Try again!!!!!")

    if won==False:
        print("Sorry you ran out of attemps.. The Secret Number is: ",random_number)



print("------------")
print("Welcome to the number guessing game")
PlayTheGame()