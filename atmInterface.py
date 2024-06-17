print("ATM Interface")
account_num=int(input("Enter account number:"))
user_pin = int(input("Enter your PIN:"))
pin = 2004
balance = 55000
if user_pin == pin:
    
        task =int(input("Press \n 1 to Withdraw money \n 2 to Credit money \n 3 to check balance \n 4 to  reset pin "))
        if task==1:
            withdrawAmount= int(input("Enter the amount to be withdrawn: \n"))
            balance = balance-withdrawAmount
            print(balance)
        elif task==2:
            creditAmount = int(input("Enter amount to be credited: \n"))
            balance = balance+ creditAmount
            print(balance)
        elif task==3:
            print(balance)
        elif task==4:
            newPin = int(input("Enter new pin: \n"))
            pin = newPin 
            print("Your pin has been resetted")  
        else:
            print("Error")
        