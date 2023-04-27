class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def model(self, value):
        self.__model = value
    

class ElectricCar(Car):
    def __init__(self, model, year, battery):
        super().__init__(model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__year
    
    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print("I can drive using")