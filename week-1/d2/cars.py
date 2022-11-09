#snake_case
#camelCase
#PascalCase

## Car class 
class Car:
    creator = "Tom"
    def __init__(self, make, model , color):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False

## output MAkE , Model , CAR
    def info(self):
        print(f"creator: {self.creator}")
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"color: {self.color}")
    

## car is running = true
    def turn_on(self):
        self.is_running = True

## print if statesments if self is running .. targets self
    def drive(self):
        if self.is_running:
            print("driving driving driving")
        else: 
            print("cannot drive because i am not started")

    @classmethod
    def change_creator(cls, new_creator):  ## argues all of the items
        cls.creator = new_creator

    @staticmethod
    def change_creator(cls , new_creator):
        color_list =['blue', 'green', 'red']
        if color in color_list:
            return True
        else:                                 ## returns a boolean
            return False


## CAR TYPES
car_a = Car('ford', 'f-150', 'black')
car_b = Car('tesla', 'model-4', 'red')

##
car_a.turn_on()
car_b.is_running = True

car_a.drive().turn_on
# Car.change_creator("tyler")

# car_a.drive()
# car_b.drive()

#print car is running true false
# print(car_a.is_running)
# print(car_b.is_running)
