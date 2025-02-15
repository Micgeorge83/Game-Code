
while True:
    num_1= float(input("Enter a number: "))
    num_2= float(input("Enter a number: "))
    operator= input("select an tenoperator +,-,*,/, %,**: ")
    try:
        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "/":
            result = num_1 / num_2
        elif operator == "%":
            result = num_1 % num_2
        elif operator == "**":
            result = num_1 ** num_2
        else:
            print("not computed")
         
    except ZeroDivisionError:
        result ="No dividy by zero!"
    except ValueError:
        result ="not a valid number"
    except Exception as e:
        result = f"does not compute {e}"

    print(f"{num_1} {operator} {num_2} = {result}")
    
    another_round = input("want to go another round yes/no?: ")
    if another_round.lower() !="yes":
        break
