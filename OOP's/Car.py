class Car:
    def __init__(self):
        self.make=None
        self.model=None
        self.year=None

    def __init__(self, make, model,year):
        self.make = make
        self.model =model
        self.year =year
    
    def displayCarDetails(self):
        print(self.make,self.model,self.year)

class Main:
    def main(self):
        Car = car("Toyota","camry","2023")
        car.displayCarDetails()

if __name__ =="__main__":
    main = Main()