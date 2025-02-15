"""Personalised Greeting Creator."""
import random as ra


# In this program we store a range of greeting strings in a list, which are then placed
# into a dictionary and used throughout the program. The main driver function (run_all)
# asks the user for a name, and then prompts the user to select either a random greeting
# or choose maunally. The choice then determines which function is called.
# to impprove? could you write the greeting to a file 

greetings = ["Hey {}, I hope you are well!",
             "Whassup {}!",
             "Have a most splendid day {}"]

dictionary_size = range(1, len(greetings)+1)

greetings_dict = dict(zip(dictionary_size, greetings))


def choose_random_greeting_template() -> str:
    """Return a random template string from the greetings dictionary.
    
    Returns:
        A random string from the greetings dictionary.
    """
    random_key = ra.choice(dictionary_size)
    return greetings_dict[random_key]


def choose_greeting_template() -> str:
    """Return a template string from greetings dictionary.
    
    Returns:
        A string from the greetings dictionary.
    """
    try:
        choice = int(input(f"Choose an integer between 1 & {max(dictionary_size)}: "))
        greeting = greetings_dict[choice]
    except ValueError:
        print("An error occured converting the input to an integer, returning a random greeting.")
    except KeyError:
        print("The value you entered is not in the dictionary, returning a random greeting.")
    else:
        return greeting
    finally:
        return choose_random_greeting_template()
    

def run_all() -> None:
    """Driver function to control flow of program.
    
    Function asks for user input for 'name' and 'greeting_style', which
    then determines the control flow of the rest of the function. Some basic
    error handling and validation of inputs is present.
    """
    name = input("Please enter your name: ")
    if not name:
        print("Name must contain at least one character")
        return

    try:
        greeting_style = int(input("Enter 1 for a random greeting, or enter 2 to choose from a list: "))
    except ValueError:
        print(f"{name.title()}, You entered an invalid choice")
        return

    if greeting_style == 1:
        random_greeting = choose_random_greeting_template()
        print(random_greeting.format(name.title()))
    elif greeting_style == 2:
        selective_greeting = choose_greeting_template()
        print(selective_greeting.format(name.title()))
    else:
        print(f"It looks like you didn't enter either 1 or 2, {name.title()}...")

        
# Run the main driver function to link it all together.
run_all()