class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return self.price>order2.price
O1=Order(input("Enter item's name: "),float(input("Enter item's price: ")))
O2=Order(input("Enter item's name: "),float(input("Enter item's price: ")))
print(O1>O2)