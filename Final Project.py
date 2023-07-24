def multiplcation( x , y ):
    return x * y

def addition( x , y ):
    return x + y


def division( x , y ):
    return x / y


def subtraction( x , y ):
    return x - y






print("    [Basic Calculator]     ")

while True:
    # take input from the user
    num1 = float(input("Your first number: "))

    print("Operation Choices.")
    print("1.   Multiplcation")
    print("2.   Addition")
    print("3.   Division")
    print("4.   Subtraction")
    choice = input("Enter choice( 1 / 2 / 3 / 4 ): ")

    num2 = float(input("Your second number: "))


    

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        
            
        

        if choice == '1':
            print(num1, "*", num2, "=", multiplcation(num1, num2))
            
        elif choice == '2':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '3':    
            print(num1, "/", num2, "=", division(num1, num2))

        elif choice == '4':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want to do another calculation(yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("That input will not work. Fix it.")