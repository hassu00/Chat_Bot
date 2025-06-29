# class atm:
#     def _init_(self,pin,balance):
#         pin:1234
#         balance:1000

#  def transaction():
class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.__year = year

    def car_for_sell(self):
        print(f"I am selling this car its model is {self.model},it is manufactured in {self.__year},and its brand is {self.brand}")

    def age_of_car(self,current_year):
        age_calculater = current_year - self.__year
        print(f"my car is {age_calculater} years old")   

    def get_year(self):
        return self.__year    

    def classic(self):
        if self.__year <= 1993 :
            print("this a classic car")
        else :
            print("this is not a classic car")   

    def summary(self):
        print(f"--summary of car--")         
        print(f"model: {self.model}")         
        print(f"year: {self.__year}")         
        print(f"brand: {self.brand}")         

my_car = car("Honda","corolla altis",1990) 
my_car.car_for_sell()       
my_car.age_of_car(2025)
my_car.classic()
my_car.summary()
print(my_car.get_year())