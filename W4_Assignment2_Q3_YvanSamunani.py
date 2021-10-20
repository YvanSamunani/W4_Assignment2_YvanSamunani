# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Omondi is starting a new business, a car renting business.
#
# Omondi starts with five different Cars.
#
# Each car has a model, a year when it was released, a year when Omondi acquired it, the money made from that car,
# the car's plate number, and the number of times that it has been in business. (It has been rented).
#As Omondi is looking into expansion, he wants to be able to rent the cars, add new cars to his collection,
# remove the cars from his collection, count the number that each car has been rented out,
# and the money made from each car.
# Please help Omondi.

class Car:
    def __init__(self, model, year_released, year_acquired, car_revenue, plate_number, working_years):
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.car_revenue = car_revenue
        self.plate_number = plate_number
        self.working_years = working_years
    def display(self):
        print("This is a ", self.model, "car!")
        print("It was released in ", self.year_released)
        print("It was acquired in ", self.year_acquired)
        print("The car generated $", self.car_revenue,)
        print("Plate number: ", self.plate_number)
        print("The has been rented for", self.working_years, "\n")


car_one_Model = input("Please enter the model of the first car: ")
car_one_year_released= input("Enter when the car was released: ")
car_one_year_acquired= input("When was the car acquired: ")
car_one_car_revenue= input("Car revenue in $ ")
car_one_plate_number= input("Car plate number: ")
car_one_working_years= input("The car has been rent for how many years: ")

car_two_Model= input("Please enter the model of the second car: ")
car_two_year_released= input("Enter when the car was released: ")
car_two_year_acquired= input("When was the car acquired: ")
car_two_car_revenue= input("Car revenue in $ ")
car_two_plate_number= input("Car plate number: ")
car_two_working_years= input("The car has been rent for how many years: ")

car_three_Model= input("Please enter the model of the third car: ")
car_three_year_released= input("Enter when the car was released: ")
car_three_year_acquired= input("When was the car acquired: ")
car_three_car_revenue= input("Car revenue in $ ")
car_three_plate_number= input("Car plate number: ")
car_three_working_years= input("The car has been rent for how many years: ")

car_four_Model= input("Please enter the model of the fourth car: ")
car_four_year_released= input("Enter when the car was released: ")
car_four_year_acquired= input("When was the car acquired: ")
car_four_car_revenue= input("Car revenue in $ ")
car_four_plate_number= input("Car plate number: ")
car_four_working_years= input("The car has been rent for how many years: ")

car_five_Model= input("Please enter the model of the fifth car: ")
car_five_year_released= input("Enter when the car was released: ")
car_five_year_acquired= input("When was the car acquired: ")
car_five_car_revenue= input("Car revenue in $ ")
car_five_plate_number= input("Car plate number: ")
car_five_working_years= input("The car has been rent for how many years: ")

car_one= Car(car_one_Model,car_one_year_released, car_one_year_acquired,car_one_car_revenue,car_one_plate_number,car_one_working_years)
car_one.display()

car_two= Car(car_two_Model,car_two_year_released, car_two_year_acquired,car_two_car_revenue,car_two_plate_number,car_two_working_years)
car_two.display()

car_three= Car(car_three_Model,car_three_year_released, car_three_year_acquired,car_three_car_revenue,car_three_plate_number,car_three_working_years)
car_three.display()

car_four= Car(car_four_Model,car_four_year_released, car_four_year_acquired,car_four_car_revenue,car_four_plate_number,car_four_working_years)
car_four.display()

car_five= Car(car_five_Model,car_five_year_released, car_five_year_acquired,car_five_car_revenue,car_five_plate_number,car_five_working_years)
car_five.display()








# See PyCharm help at https://www.jetbrains.com/help/pycharm/


