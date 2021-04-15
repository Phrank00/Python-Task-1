import random

database = {}
cash_balance = 5000


def init():
    print("Welcome to Bank Checkers")
    welcome = int(input("Press 1 to login or 2 to register\n"))
    if welcome == 1:
        login()
    elif welcome == 2:
        register()
    else:
        print("Invalid Input, Please try again")
        init()


def login():
    print("Log in to your account")

    user_login = int(input("Please enter your account number\n"))
    user_password = input("Please enter your password\n")

    for account_number, user_details in database.items():
        if account_number == user_login and user_details[3] == user_password:
            bankOperations(user_details)
        else:
            print("Invalid Username or Password. Please try again")
            login()


def register():
    print('Create your account')
    email = input("Please enter your email address\n")
    first_name = input("Please enter your first name\n")
    last_name = input("Please enter your last name\n")
    password = input("Please create a password\n")
    account_number = random.randrange(2222222222, 9999999999)
    print("Registration Complete.\n Your account number is %d" % account_number)

    database[account_number] = [first_name, last_name, email, password]

    login()


def bankOperations(user_details):
    print("Welcome %s %s" % (user_details[0], user_details[1]))
    selected_options = int(input("Please select an option: (1) Withdrawal (2) Cash Deposit "
                                 "(3) Change password (4) Complaint (5)Logout (6) Exit\n"))

    if selected_options == 1:
        withdrawal_options(user_details)
    elif selected_options == 2:
        deposit_options(user_details)
    elif selected_options == 3:
        change_password(user_details)
    elif selected_options == 4:
        complaint(user_details)
    elif selected_options == 5:
        logout()
    elif selected_options == 6:
        exit()
    else:
        print("Invalid Option Selected")
        bankOperations(user_details)


def withdrawal_options(user_details):
    print("*****Withdrawal*****")
    withdrawal_amount = (int(input("How much will you like to withdraw?\n")))

    if withdrawal_amount <= cash_balance:
        print("Take your cash\n")
        current_balance = (cash_balance - withdrawal_amount)
        print("Your current balance is %d" % current_balance)

    elif withdrawal_amount > cash_balance:
        print("Insufficient Funds")


    progress = int(input("Will you like to perform any other transactions? (1) Yes (2) No\n"))
    if progress == 1:
        bankOperations(user_details)
    elif progress == 2:
        logout()

def deposit_options(user_details):
    print("*****Cash Deposits only*****")
    deposit_amount = (int(input("How much will you like to deposit?\n")))
    current_balance = (cash_balance + deposit_amount)
    print("Deposit Successful. Your Current Balance is %d" % current_balance)

    progress = int(input("Will you like to perform any other transactions? (1) Yes (2) No\n"))
    if progress == 1:
        bankOperations(user_details)
    elif progress == 2:
        logout()


def change_password(user_details):
    old_password = input("Enter your old password\n")
    if old_password == user_details[3]:
        new_password = input("Enter your new password\n")
        confirm_new_password = input("Confirm your new password\n")
        if new_password == confirm_new_password:
            print("Password changed")
            user_details[3] = new_password
        else:
            print("Passwords do not match. Pls try again")
            change_password()
    else:
        print("Incorrect Password. Please try again")
        change_password()

    progress = int(input("Will you like to perform any other transactions? (1) Yes (2) No\n"))
    if progress == 1:
        bankOperations(user_details)
    elif progress == 2:
        logout()



def complaint(user_details):
    complaint_1 = input("What issue will you like to report?\n")
    print("Complaint is noted. You will get a response via email shortly.")

    progress = int(input("Will you like to perform any other transactions? (1) Yes (2) No\n"))
    if progress == 1:
        bankOperations(user_details)
    elif progress == 2:
        logout()

def logout():
    print("Thank You for banking with us")



########### ACTUAL BANKING SYSTEM ################

init()
