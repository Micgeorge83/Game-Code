""""# ---Points for improvement---

# - Extend this program to ask the for the name in a safer way, perhaps with a while loop?

# - Write additional logic into the gameplay loop so that each guess is stored
#   in a list and then if the user makes a duplicate guess, they are warned?

# - Make the gameplay loop give a warning if a number is guessed that is outside
#   the range of what is allowed? (Say if the low, high is 1, 10 but the user guesses a 12 for example).

# - Write a function to read the existing score file to the user before gameplay commences.

# - Difficult.. Make this a 2 player game!"""





import random as ra
from datetime import datetime



def create_save_file_text(name: str, guesses: int, lowest: int, highest: int)-> str:
    now = datetime.now()
    formatted_now = datetime.strftime(now, format="%H:%M:%S %d-%B-%Y")
    score_string = "Player: {}. Guesses: {}, given {} number choices.---{}\n".format(name, guesses, (highest - lowest)+1,formatted_now)
    return score_string


def write_text_to_file(filename: str, text: str, mode: str= "a"):
    with open (filename, mode=mode) as file:
        file.write(text)


def retrieve_lower_upper_nums()->tuple:
    attempts_to_enter_valid_nums = 3
    current_attempts = 0

    while current_attempts < attempts_to_enter_valid_nums:
        current_attempts += 1
        try:
            low = int(input("Enter a lower bound: "))
            high = int(input("Enter an upper bound: "))
        except ValueError:
            print("Invalid format dumbass!")
            continue
        else:
            if low < high:
                return low, high
            else:
                print("Think about what you just did, low cannot be bigger than the high..")
                continue
    else:
        print("Attempts exceeded, defaulting to 1, 10, cause I ain't got all day for your dumbassery.")
        return 1,10
    

def establish_random_num(lowest: int, highest: int)->int:
    return ra.randint(lowest, highest)


def main_gameplay(random_number) -> int:
   
    attempts = 1
    guess = int(input("Enter guess here: "))
    while guess != random_number:
        attempts += 1
        if guess > random_number:
            guess = int(input("Lower:... "))
        elif guess < random_number:
            guess = int(input("Higher:... "))
        else:
            print("Correct!")
    return attempts



def main(filename: str)-> None:
    name = input("Enter your name: ").title()
    if not name:
        print("No name entered, exiting")
        return
    
    low,high = retrieve_lower_upper_nums()
    print(f"Low is set at {low} and high is set at {high}.\n")
    
    random_number = establish_random_num(low,high)
    
    score= main_gameplay(random_number)
    print(f" You took {score} attempts to guess {random_number}.")

    file_text = create_save_file_text(name, score, low, high)

    write_text_to_file(filename,file_text)
    

if __name__ == "__main__":
    filename = "scores.txt"
    main(filename)

