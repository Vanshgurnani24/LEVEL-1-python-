print("Time to play hangman")
print("Start Guessing:.......")
word='future' #word that we need to guess

guesses='' #variable with an empty value
attempts=10 #max attempts a user can make while guessing the word

#while loop that checks if the attempts are more than zero
while attempts>0:
    failed=0 #initializes default value for failed as 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1

    if failed==0:
        print("You won the game.")
        break
    guess=input("guess the character")
    guesses+=guess #appends the guesses with the previous input


    if guess not in word: #if input characted is not present as the character of guess in word it will reduce the no of attempts by 1
        attempts-=1
        print("Wrong")
        print("You now have ",attempts," attempts remaining")
        if attempts==0:
            print("You loose")
