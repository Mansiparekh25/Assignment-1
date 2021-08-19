
import Account
Customer=[]
Dict={}
def cust():

    cust =input("please enter username: ")
    cust=cust.strip().upper()


    if cust in Customer:
        Account.bank_act()
        print("WELCOME", cust)
        act()
    else:
         print("please register")
         Account.bank_act()
         Customer.append(cust.strip().upper())
         exit()

def act():

    print("choose your Action: ")
    print("(1)Create account (2)Choose Account (3)Quit Application")
    action=int(input("action(?): "))

    if action==1:
      Account.bank_act()

    if action==2:
        choose_act()
    if action==3:
        exit()

    else:
       print("Please Enter valid choice")
    act()


def choose_act():

        print("choose account from below")
        print(*Dict,sep="\n")
        account_number=input("select account(?): ")
        if account_number not in(Dict):
            Dict.update({account_number: 100})
            print("choose valid account")
        else:
            print("select Transction Action: ")
            print("(1)cash deposit (2)cash withdraw (3)Check balance")
            action_Tran = int(input("action(?): "))
            if action_Tran==1:
                deposit_amount = input("Enter the amount for deposit: ")
                if deposit_amount.isnumeric():
                    if int(deposit_amount) <= 0:
                        print("Invalid deposit amount")
                        act()

                    elif int(deposit_amount) > 0 and Dict.get(account_number) + int(deposit_amount) < 100:
                        print("minimum balance should be 100")
                        act()
                    else:
                        balance = Dict.get(account_number) + float(deposit_amount)
                        Dict.update({account_number: balance})
                        print("Account number: {} \n Balance: {}".format(account_number, Dict.get(account_number)))
                        act()
                else:
                  print("Please enter valid deposit amount")
                  act()
            if action_Tran==2:
                withdraw_amount = input("enter the amount for withdraw: ")
                if withdraw_amount.isnumeric():
                     if int(withdraw_amount) <= 0:
                        print("Invalid withdraw amount")
                        act()
                     if int(withdraw_amount) > Dict.get(account_number):
                        print("insufficient balance!")
                        act()
                     elif Dict.get(account_number)- int(withdraw_amount) < 100:
                        print("you exceed the limit")
                        act()
                     else:
                        balance = Dict.get(account_number) - int(withdraw_amount)
                        Dict.update({account_number: balance})
                        print("Account number: {} \n Balance: {}".format(account_number, Dict.get(account_number)))
                        act()
                else:
                   print("Please enter valid withdraw amount")
                   act()
            if action_Tran==3:
                print("your available balance for {} is {}: ".format(account_number, Dict.get(account_number)))
                act()
            else:
                print("Please Enter valid choice")
        act()







if __name__ == "__main__":
         cust()
