import main


def bank_act():

       account_number = input("Add your Account Number: ")
       if account_number.isnumeric():

            if account_number in (main.Dict):
                print("Your account is already there")

            else:
                print("Account is Created")
                main.Dict .update({account_number: 100})
                print("your initial balance is:",main.Dict.get(account_number))
                main.act()
       else:
           print("select valid account_number")
           bank_act()
if __name__ == "__Account__":
         bank_act()

