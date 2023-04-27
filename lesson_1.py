class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, model, year, color, winks_range):
        Transport.__init__(self, model, year, color)
        self.winks_range = winks_range

    def fly(self, country):
        print(f"{self.model} летит в {country}")


class Car: #Шаблон
    number_of_weels = 4 # Атрибуты поля
    # __init__ - Конструктор
    # model, year, color - Входящие переменные
    # self -Ссылка на обьект
    # self.model - атрибуты, поля обьекта
    def __init__(self, model, year, color, penalties=0.0):
        Transport.__init__(self, model, year, color) 
        self.penalties = penalties

    def drive(self, city): #Метод
        print(f"{self.model} едет в {city}")

class Truck(Transport):
    def __init__(self, model, year, color, penalties, load_capacity):
        Car.__init__(self, model, year, color)
        self.load_capacity = load_capacity

    def load_capacity(self, weight):
        if weight > self.load_capacity:
            print(f"Ты не можещь загрузит груз, он превышает грузоподемность {self.load_capacity} ")
        else:
            print(f"ГРуз загружен {self.model}. Вес - {weight}")

            
transport = Transport("Transport", 2020, "Green")

print(Car.number_of_weels)


tesla_car = Car("Tesla Model X", 2023, "White", "1000") # ОбЬект
print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")
tesla_car.color = "Black"
print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")
tesla_car.change_color("Blue")
print(tesla_car.number_of_weels)
print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")
tesla_car.drive("Ош")

Car.number_of_weels = 8
kamaz = Car(model="Kamaz", year=1999, color="red", penalties=2000, load_capacity=12000)
print(f"Model: {kamaz.model} Year: {kamaz.year} Color: {kamaz.color} Penalties: {kamaz.penalties} load_capacity: {12000}")
kamaz.drive("Бишкек")
print(kamaz.number_of_weels)
kamaz.load_capacity(11000)