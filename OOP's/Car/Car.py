class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def displayCarDetails(self):
        print(self.make, self.model, self.year)

class Main:
    def main(self):
        car_instance = Car("Toyota", "Camry", "2023")
        car_instance.displayCarDetails()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
