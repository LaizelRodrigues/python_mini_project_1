"""
description
author:=Laizel Rodrigues
MISIS:=M00910091
"""
#This is a python code based on an ATM machine, that will withdraw, deposit money and show current balance

choice = input("Do you want to run the program?(y/Y):")
while choice == "y" or choice == "Y":
    print("Welcome to the ATM Machine \n","Main menu \n","1.Withdraw cash \n 2.Deposit cash \n 3.View account balance") #print the menu
    c=int(input("Enter your choice(1,2,3):"))
    Name=input("Enter your name:")
    Account_balance=10000
    maximum_amount=5000
    pins=[1234,1233,1222]
    pin=int(input("Enter your 4 digit pin number:"))
    if (pin in pins):
        print(c)
    else:
        print("Invalid pin,please try again and enter a valid pin")
        break
    #To withdraw money from the ATM
    if(c==1):
        withdraw=int(input("Enter amount to be withdrawn:"))
        current_balance = Account_balance - withdraw
        if (withdraw<=maximum_amount):
                print("Please take your amount:",withdraw, "Thank you","your current account balance is",current_balance)
        else:
            print("Invalid amount,you can only withdraw up to 5000.")
     # To deposit money into the ATM
    elif(c==2):
        amt=int(input("Enter amount to deposit:"))
        deposit=input("Is this entry correct,Yes(y/Y), or No(N/n)?"+ str(amt) + " ")
        current_balance = Account_balance+amt
        if deposit == "Y" or deposit == "y":
            print("amount deposited successfully, your current amount is",current_balance)
        else:
            print("Transaction cancelled, try again later")
     #To view current account balance
    elif(c==3):
        print("Your account balance is:",Account_balance)
    else:
        print("Invalid menu option, please select 1,2 or 3")    
    choice = input("Do you want to continue using the ATM?(y/Y)")

#end
