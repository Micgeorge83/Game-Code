import random as ra 


def choose_question_type()-> str:
    question_type = ["Addition",  "Subtraction" , "Multiplication" ,"Mix"]
    print (f"choose a question type: {' '.join(question_type)}\n ")
    choice = input("Pick your posion: ").title()

    while choice not in question_type:
        choice = input("Stop, remove head from rectum and try this again:  ").title()
    else:
        return choice


def  choose_difficulty_level()-> int:
    while True:
        try:
            difficulty_level = int(input("From a scale of 1-5, how hard you want it?:  "))
        except ValueError:
            print("format does not commpute, wake ur other braincell and try again!")
            continue
        else:
            if difficulty_level in range(1,6):
                return difficulty_level
            print ('Look at the scale and try again')


def choose_number_of_questions()-> int:
    try:
        num_of_questions = int(input("How long you wanna go for?"))
    except ValueError:
        print("lamesauce... we are rollin the default 10")
        return 10
    else:
        if num_of_questions <= 0:
            print("all sorts of stupid.. you get the default of 10")
            return 10
        return num_of_questions


def generate_numbers_for_question(difficulty_level: int)-> tuple:
    operand_a = ra.randint(difficulty_level*2, difficulty_level*20)
    operand_b = ra.randint(difficulty_level*2, difficulty_level*20)
    return operand_a, operand_b



def addition_question(operand_a: int, operand_b: int) ->int:
    try:
        question = int(input(f"What is {operand_a} + {operand_b}= "))
    except ValueError:
        print("Invalid format, moving on...")
        return False
    else:
        return True if (question == operand_a + operand_b) else False

def subtraction_question(operand_a: int, operand_b: int) ->int:
    try:
        question = int(input(f"What is {operand_a} - {operand_b}= "))
    except ValueError:
        print("Invalid format, moving on...")
        return False
    else:
        return True if (question == operand_a - operand_b) else False

def multiplication_question(operand_a: int, operand_b: int) ->int:
    try:
        question = int(input(f"What is {operand_a} * {operand_b}= "))
    except ValueError:
        print("Invalid format, moving on...")
        return False
    else:
        return True if (question == operand_a * operand_b) else False





def main_game_loop(question_type: str, num_of_questions: int, difficulty_level: int)-> int:
    num_of_correct_answers = 0
    for i in range (1, num_of_questions+1):
        operand_a, operand_b = generate_numbers_for_question(difficulty_level)
        print(f"Question {i}")
        if question_type == "Addition":
            response = addition_question(operand_a, operand_b)
        
        elif question_type == "Subtraction":
            response =  subtraction_question(operand_a, operand_b)
        
        elif question_type == "Multiplication":
            response = multiplication_question(operand_a, operand_b)
        
        elif question_type == "Mix":
           q_types = [addition_question,subtraction_question, multiplication_question]
           response = ra.choice(q_types)(operand_a, operand_b)
        
        if response:
            print("That is Correct\n")
            num_of_correct_answers += 1
        else:
            print(" WRONG..SMDH.....dumbass\n")

    return num_of_correct_answers



def main() ->None:
    question_type = choose_question_type()
    if question_type == "Mix":
        print("We gonna mix it up!\n")
    else:
        print(f"You have made your choice of {question_type}\n ")
    
    difficulty_level = choose_difficulty_level()
    print (f"You have made your chose of {difficulty_level}\n")

    num_of_questions = choose_number_of_questions()
    print(f"You got {num_of_questions} questions ahead of you, venture well my fellow nerd! \n")

    correct_answers = main_game_loop(question_type, num_of_questions, difficulty_level)
    print(f"You made it out alive with {correct_answers} correct answers out of {num_of_questions} questions")

if __name__== "__main__":
    main()
