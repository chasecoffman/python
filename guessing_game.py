
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def secretWord():
    secret_word = "guess"
    user_guess = ""
    guess_counter = 0
    user_limit = 3
    loser = False

    print(color.BLUE + color.BOLD + "What is the secret word? " + color.END)
    while user_guess != secret_word and not(loser):
        if guess_counter < user_limit:
            user_guess = input("Enter " + color.UNDERLINE + "guess" + color.END + ":")
            guess_counter += 1
        else:
            loser = True

    if loser:
        print(color.RED + "You lose!" + color.END)
    else:
        print(color.GREEN + "You win!")

    while loser == True:
        replay = input("Try Again? " + color.YELLOW + color.BOLD + "YES(1) NO(2)")
        if replay == "1":
            secretWord()
        else:
            loser == False
            break

secretWord()



