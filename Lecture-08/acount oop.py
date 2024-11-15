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
        print(credit,"has been credited")
        return self.acc_bal
    def balance(self):
        return self.acc_bal
person=Bank("12345554",120000,"tanisha_1234")
print("Bank Balance: ",person.balance())