#員工
class Employee:
    def __init__(self, name, years_of_service, work_hours_per_day, hourly_rate):
        self.name = name
        self.years_of_service = years_of_service
        self.work_hours_per_day = work_hours_per_day
        self.hourly_rate = hourly_rate
    #員工名字
    def get_name(self):
        return self.name
    #員工年資
    def get_years_of_service(self):
        return self.years_of_service
    #員工工時
    def get_work_hours_per_day(self):
        return self.work_hours_per_day
    #計算月薪
    def calculate_monthly_salary(self):
        days_worked_per_month = 20  
        monthly_salary = self.work_hours_per_day * days_worked_per_month * self.hourly_rate
        return monthly_salary
    #增加工時
    def increase_work_hours(self, additional_hours):
        self.work_hours_per_day += additional_hours
    #增加年資
    def increase_years_of_service(self, additional_years):
        self.years_of_service += additional_years

# 建立三個員工並呼叫六個副函式
employee1 = Employee("Judy", 5, 160, 20)
print("員工:", employee1.get_name())
print("年資", employee1.get_years_of_service())
print("工時:", employee1.get_work_hours_per_day())
print("月薪:", employee1.calculate_monthly_salary())
employee1.increase_work_hours(2)
employee1.increase_years_of_service(1)
print("增加後工時:", employee1.get_work_hours_per_day())
print("增加後年資:", employee1.get_years_of_service())

employee2 = Employee("Justin", 3, 150, 18)
print("\n員工:", employee2.get_name())
print("年資:", employee2.get_years_of_service())
print("工時:", employee2.get_work_hours_per_day())
print("月薪:", employee2.calculate_monthly_salary())
employee2.increase_work_hours(1)
employee2.increase_years_of_service(2)
print("增加後工時:", employee2.get_work_hours_per_day())
print("增加後年資:", employee2.get_years_of_service())

employee3 = Employee("Ray", 7, 145, 22)
print("\n員工:", employee3.get_name())
print("年資:", employee3.get_years_of_service())
print("工時:", employee3.get_work_hours_per_day())
print("月薪:", employee3.calculate_monthly_salary())
employee3.increase_work_hours(3)
employee3.increase_years_of_service(1)
print("增加後工時:", employee3.get_work_hours_per_day())
print("增加後年資:", employee3.get_years_of_service())

#飲料
class Drink:
    def __init__(self, name, price, has_boba, eco_friendly_cup):
        self.name = name
        self.price = price
        self.has_boba = has_boba
        self.eco_friendly_cup = eco_friendly_cup
#繼承
class HotColdDrink(Drink):
    def __init__(self, name, price, has_boba, eco_friendly_cup, hot_or_cold):
        super().__init__(name, price, has_boba, eco_friendly_cup) 
        self.hot_or_cold = hot_or_cold

    def get_drink_name(self):
        if self.hot_or_cold.lower() == "hot":
            return f"\n熱的 {self.name}"
        elif self.hot_or_cold.lower() == "cold":
            return f"\n冷的 {self.name}"
        else:
            return f" {self.name} "

    def adjust_sweetness(self, sweetness_level):
        return f"糖度:{sweetness_level}"

    def adjust_price(self, new_price):
        self.price = new_price
        return f"飲料價格:{new_price}"

    def has_boba_info(self):
        if self.has_boba:
            return "有加波霸"
        else:
            return "沒有加波霸"    

    def eco_friendly_cup_info(self):
        if self.eco_friendly_cup:
            return "有環保杯"
        else:
            return "沒有環保杯" 

# 建立三杯飲料並呼叫六個副函式
drink1 = HotColdDrink("綠茶", 35, True, True, "Hot")
print(drink1.get_drink_name())
print(drink1.adjust_sweetness("少糖"))
print(drink1.has_boba_info())
print(drink1.eco_friendly_cup_info())
print(drink1.adjust_price(35))

drink2 = HotColdDrink("冰美式", 65, False, False, "Cold")
print(drink2.get_drink_name())
print(drink2.adjust_sweetness("無糖"))
print(drink2.has_boba_info())
print(drink1.eco_friendly_cup_info())
print(drink2.adjust_price(65))

drink3 = HotColdDrink("奶茶", 50, True, True, "Hot")
print(drink3.get_drink_name())
print(drink3.adjust_sweetness("半糖"))
print(drink3.has_boba_info())
print(drink1.eco_friendly_cup_info())
print(drink3.adjust_price(50))

