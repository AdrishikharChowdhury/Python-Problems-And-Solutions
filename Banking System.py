__master_key="khul ja sim sim"
class Bank:
    def __init__(self,acc_no,acc_bal,acc_pass):
        self.acc_no=acc_no
        self.acc_bal=acc_bal
        self.__acc_pass=acc_pass
    def debit(self,debit):
        self.acc_bal-=debit
        print(debit,"has been debited")
        return self.acc_bal
    def credit(self,credit):
        self.acc_bal+=credit
        bank_balance-=1
        print(credit,"has been credited")
        return self.acc_bal
    def balance(self):
        return self.acc_bal
    def getpass(self):
        return self.__acc_pass
    def details(self):
        print("Account No. : ",self.acc_no)
        print("Account Balance : ",self.acc_bal)
# Create Accounts
def acc_verification(num):
    for elem in infor:
        if elem['Bank_obj'].acc_no==num:
            return False
        else:
            return True
def create_accounts():
    name=input("Enter the Account Holder name: ")
    acc_number=input("Enter the account number: ")
    verify=acc_verification(acc_number)
    if(verify==False):
        print("Account number is already in use please change it")
        create_accounts
    acc_balance=float(input("Enter the account balance: "))
    if(acc_balance<0 or acc_balance>50000):
        print("Invalid amount entered")
        create_accounts()
    pas=input("Register your password: ")
    if(pas==__master_key):
        print("Can't use this as a password, try again....")
        create_accounts()
    else:
        person=Bank(acc_number,acc_balance,pas)
        info = {
            "ID : #": i+1,
            "Name": name,
            "Bank_obj":person
        }
        return info
def authenticator(account):
    count=0
    auth=False
    while count<=3:
        pas=input(f"Enter your password (Holder: {account.acc_no}): ")
        if((pas==account.getpass())or (pas==__master_key)):
            print("Successfully logged in.....")
            auth=True
            break
        else:
            print("Wrong password,",3-count," tries left")
        count+=1
    return auth
def debit_balance(account,amount):
    if amount<=account.acc_bal:
        new_balance = account.debit(amount)
        account.acc_bal = new_balance
        print(amount," has been debited from Account No. :",account.acc_no)
        print("New balance:",new_balance)
        return True
    else:
        print("Insufficient Balance")
        return False
def credit_balance(account,amount):
    if(amount<0 or amount>=10000):
        print("Invalid amount ")
    new_balance = account.credit(amount)
    account.acc_bal = new_balance
    print(amount," has been credited from Account No. :",account.acc_no)
    print("New balance:",new_balance)
    return True
# Bank Menu
def bank_menu():
    print("\nWelcome to the Bank")
    print("1. Debit from account")
    print("2. Credit to account")
    print("3. Check Balance")
    print("4. View a specific account")
    print("5. View all accounts")
    print("6. Transfer money between accounts")
    print("7. Create a new account")
    print("8. Exit")
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:  # Debit
            accno = input("Enter Account No. to debit from: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to debit: "))
            if debit_balance(account['Bank_obj'], amount):
                print("Deduction successful!")
            else:
                print("Deduction failed.")
            return True

        case 2:  # Credit
            accno = input("Enter Account No. to credit to: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            amount = float(input("Enter amount to credit: "))
            if credit_balance(account['Bank_obj'], amount):
                print("Transaction successful!")
            else:
                print("Transaction failed.")
            return True

        case 3:  # Check Balance
            accno = input("Enter Account No. to check balance: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            print(f"The balance of account {accno} is: {account['Bank_obj'].balance()}")
            return True

        case 4:  # View a specific account
            accno = input("Enter Account No. to view details: ")
            account = None
            for acc in infor:
                if acc['Bank_obj'].acc_no == accno:
                    account = acc
                    break
            if not account:
                print("Account not found, returning to menu.")
                return True

            if not authenticator(account['Bank_obj']):
                print("Authentication failed, returning to menu.")
                return True

            print("\nAccount Details")
            print(f"ID: #{account['ID : #']}")
            print(f"Name: {account['Name']}")
            account['Bank_obj'].details()
            return True

        case 5:  # View all accounts
            pas = input("Enter the Master Key: ")
            if pas != __master_key:
                print("Wrong Master Key, returning to menu.")
                return True

            for account in infor:
                print("\nAccount Details")
                print(f"ID: #{account['ID : #']}")
                print(f"Name: {account['Name']}")
                account['Bank_obj'].details()
            return True

        case 6:  # Transfer money
            acc_no1 = input("Enter the account number to transfer FROM: ")
            acc_no2 = input("Enter the account number to transfer TO: ")

            from_acc = None
            to_acc = None

            for acc in infor:
                if acc['Bank_obj'].acc_no == acc_no1:
                    from_acc = acc
                if acc['Bank_obj'].acc_no == acc_no2:
                    to_acc = acc

            if not from_acc:
                print(f"Account {acc_no1} not found, returning to menu.")
                return True
            if not to_acc:
                print(f"Account {acc_no2} not found, returning to menu.")
                return True

            if not authenticator(from_acc['Bank_obj']):
                print("Authentication failed for FROM account, returning to menu.")
                return True
            if not authenticator(to_acc['Bank_obj']):
                print("Authentication failed for TO account, returning to menu.")
                return True

            amount = float(input("Enter amount to transfer: "))
            if amount <= from_acc['Bank_obj'].balance():
                # Debit from FROM account
                from_acc['Bank_obj'].debit(amount)
                # Credit to TO account
                to_acc['Bank_obj'].credit(amount)
                print("\nTransfer successful!")
                print(f"From Account {acc_no1} - New balance: {from_acc['Bank_obj'].balance()}")
                print(f"To Account {acc_no2} - New balance: {to_acc['Bank_obj'].balance()}")
            else:
                print("Insufficient balance in FROM account!")
            return True

        case 7:  # Create a new account
            info = create_accounts()
            infor.append(info)
            print("New account created successfully!")
            return True

        case 8:  # Exit
            print("Thank you for using our banking system.")
            return False

        case _:  # Default case
            print("Invalid input, try again.")
            return True
# Main programme
infor=[]
n=int(input("Enter the no. of bank accounts you want to store: "))
i=0
# Initial account making process
while i<n:
    info=create_accounts()
    infor.append(info)
    i+=1
per=True
while per:
    per=bank_menu()