class Item:
    pay_rate = 0.8        # pay rate variable showing amount to be paid after discount.
    all = [ ]             # created a list to append all instance( value-attributes created )

    def __init__(self, name: str , price: float, quantity = 0):

        # Using assert statenent to cross check that the price and quality are never negative
        # Assert statements display assertion errors such as if the condition price & quantity >= 0 is False. 
        assert price >=0, f"Price {price} should be greater/equal to 0"
        assert quantity >=0, f"Quantity {quantity} should be greater/equal to 0"

        #assiging varibale names to the attributes 
        self.name = name
        self.price = price 
        self.quantity = quantity

        # adding all Class instance elements to a list to enable easy filtering
        # Will use the self in the append(self) method since self intaciates all Class Instances when created
        Item.all.append(self)




    def get_tot_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate



first2 = Item('tourch', 200, 9)
first1 = Item('radio', 200, 1)


print(Item.all)



# first1 = Item('radio', 200, 1)
# first1.apply_discount()
# print(first1.price) 
 
# first2 = Item('tourch', 200, 9)
# first2.pay_rate = 0.7
# first2.apply_discount()
# print(first2.price)

# print(first1.get_tot_price())
# print(Item.pay_rate)