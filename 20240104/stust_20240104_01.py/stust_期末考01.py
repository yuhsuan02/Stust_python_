class FriedChicken:
    def __init__(self, flavor, part, amount, price, is_crispy):
        self.flavor = flavor
        self.part = part
        self.amount = amount
        self.price = price
        self.is_crispy = is_crispy

    def display_details(self):
        print(f"\n口味: {self.flavor}")
        print(f"部位: {self.part}")
        print(f"數量: {self.amount}")
        print(f"價格: {self.price}")
        print(f"酥脆? {'是' if self.is_crispy else '不是'}")

    # 炸雞的數量
    def increase_quantity(self, increment):
        self.quantity += increment
        print(f"Quantity increased by {increment}. New quantity: {self.quantity}")
    
    #價格
    def change_price(self, new_price):
        self.price = new_price
        print(f"Price changed to {self.price}")

    #酥脆
    def set_crispiness(self, is_crispy):
        self.is_crispy = is_crispy
        print(f"Crispiness set to {'Crispy' if self.is_crispy else 'Not crispy'}")


# 建立四個物件，/口味/部位/辣度/價格/酥脆
chicken_1 = FriedChicken("一般正常", "雞腿", 3, 120, True)
chicken_2 = FriedChicken("辣味", "雞翅", 5, 130, False)
chicken_3 = FriedChicken("BBQ", "雞胸", 2, 100, True)
chicken_4 = FriedChicken("蜂蜜芥末醬", "雞排", 4, 240, False)

# 顯示出四個物件
chicken_1.display_details()
chicken_2.display_details()
chicken_3.display_details()
chicken_4.display_details()

# 改變物件
chicken_1.increase_quantity(1)  
chicken_2.change_price(9.49)  
chicken_3.set_crispiness(True) 

