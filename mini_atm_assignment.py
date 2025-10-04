########## flow Checklist:

# 1- start with a fixed amount variable amount_balance

# 2- display a menu of (1-4) options and input for user to choose option

# 3- trigger action based on user input (1-4), using loop and condionals

# 3.1- print account balance
# 3.2- add deposit after validating deposit input
# 3.3- subtract withdrawal after validating withdrawal input
# 3.4- exit menu 


def mini_atm(account_balance):
    ### Mini Atm Simulator Function that displays a menu with user input to trigger atm options


    ### assigning a menu
    menu = f"""

    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit

    """

    ### printing section: welcoming message + balance + menu
    print("``````````````````````````````````````````````````````````")
    print("Welcome to the ATM")
    print("Your balance is: ", account_balance)
    print(menu)


    ### Taking user input to trigger an option
    input_option = eval(input("Choose an option: "))

    ### Looping user input_options to trigger (1-4) actions on the menu:
    while input_option != 4:

    ### invalid out of menu range (1 - 4)
        if input_option < 1 or input_option > 4: 

            print("``````````````````````````````````````````````````````````")
            print("\n", "Choose a valid option", "\n", sep="")

    ### menu option 1: printing account balance
        elif input_option == 1:                 

            print("``````````````````````````````````````````````````````````")
            print(f"Your balance is {account_balance}", end="\n")

    ### menu option 2: adding money to account balance
        elif input_option == 2:                 

            print("``````````````````````````````````````````````````````````")
            deposit_amount = eval(input("Enter amount to deposit: "))

    #### limiting deposits to positive amounts
            if deposit_amount > 0:              
                account_balance += deposit_amount
                print("Deposit successful. New balance = ", account_balance)
            else:
                print("Deposit unsuccessful. Choose a valid amount to deposit")

    ### menu option 3: subtracting money from account balance
        elif input_option == 3:                 
            print("``````````````````````````````````````````````````````````")
            withdraw_amount = eval(input("Enter amount to withdraw: ")) 
            
    ### limiting withdrawals to positive amounts
            if withdraw_amount <= 0:             
                print("Withdrawal unsuccessful. Choose a valid amount to withdraw")
            elif withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print("Withdrawal successful. New balance = ", account_balance)
            else:
                print("Insufficient funds!")

    ### while input != 4: looping print section:
        print("``````````````````````````````````````````````````````````")
        print("Welcome to the ATM")
        print("Your balance is: ", account_balance)
        print(menu)
        input_option = eval(input("Choose an option: "))

    ### menu option 4: input == 4: breaking out of menu to exit
    print("Goodbye!")
    print("``````````````````````````````````````````````````````````")
    



mini_atm(1170)