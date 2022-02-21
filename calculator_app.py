def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide
              }
def calculator():
    num1 = float(input("first number "))

    # to print all keys which contains all operands
    for key in operations:
        print(key)
    chosen_key = input("what operations do you want to carryout ")


    num2 = float(input("second number"))

    # when a key access a function value we use the variable as a caller like below
    calculation_function = operations[chosen_key]
    answer = calculation_function(num1, num2)

    print(f"{num1} {chosen_key} {num2} = {answer}")
    continue_calculation = input('type y to continue, type n to to stop calculation or S to start new calculation')
    if continue_calculation == 'y':
        common = True
        while common:
            num = float(input("Enter next number "))
            for key in operations:
                print(key)
            chosen_key = input("what operations do you want to carryout ")
            calculation_function = operations[chosen_key]
            answer_1 = calculation_function(answer, num)
            print(f"{answer} {chosen_key} {num} = {answer_1}")
            continue_calculation = input('type y to continue, type n to to stop calculation, S to start new calcuation ')
            if continue_calculation == 'n':
                break
            elif continue_calculation =='s':
                calculator()
    elif continue_calculation == 'n':
        common = False
    elif continue_calculation == 's':
        calculator()
#     this common above is called a FLag
calculator()