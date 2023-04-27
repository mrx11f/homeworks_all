class Address:
    def __init__(self, city, street, home_number) -> None:
        self.__city = city
        self.__street = street
        self.__home_number = home_number  

    @property
    def city(self):
        return self.city  

class Animal:
    def __init__(self, name, age, address) -> None:
        self.__name = name
        self.__age = age
        self.address = address
    def get_name(self):
        return self.get_name

# cat = Animal("Barsik", 3, "Osh", "Lenina", "101")
# print(f"Name: {cat.name}\nAge: {cat.age}\nAddress {cat.city}, street {cat.street}, №{cat.home_number}")

    def set_name(self, value):
        self.__name = value

    def set_age(self, value):
        if value < 1:
            self.__age = value
        else:
            print("меньше одного не можеть")


    def info(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nAddress {self.address.city}, street {self.address.street}, №{self.address.home_number}")

address1 = Address("Bishkek", "Ibraimova", 103)
cat = Animal("Barsik", 3, address1)


# cat.info()
# cat.set_age = (10)
# cat.info()
# print(cat.get_name())

