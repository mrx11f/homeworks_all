class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    def set_cpu(self, cpu):
        self.__cpu = cpu
        
    def set_memory(self, memory):
        self.__memory = memory
        
    def get_cpu(self):
        return self.__cpu
    
    def get_memory(self):
        return self.__memory
    
    def make_computations(self):
        return self.__cpu + self.__memory
    
    def __str__(self):
        return f"Computer: CPU - {self.__cpu}, Memory - {self.__memory}"
    
    def __eq__(self, other):
        return self.__memory == other.get_memory()
    
    def __ne__(self, other):
        return self.__memory != other.get_memory()
    
    def __lt__(self, other):
        return self.__memory < other.get_memory()
    
    def __le__(self, other):
        return self.__memory <= other.get_memory()
    
    def __gt__(self, other):
        return self.__memory > other.get_memory()
    
    def __ge__(self, other):
        return self.__memory >= other.get_memory()
    
    
class Phone:
    def __init__(self):
        self.__sim_cards_list = []
        
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
        
    def get_sim_cards_list(self):
        return self.__sim_cards_list
    
    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number-1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} - {sim_card}")
    
    def __str__(self):
        return f"Phone: {self.__sim_cards_list}"
    
    
class SmartPhone(Computer, Phone):
    def use_gps(self, location):
        print(f"Проложен маршрут до {location}")
    
    def __str__(self):
        return f"SmartPhone: CPU - {self.get_cpu()}, Memory - {self.get_memory()}, SIM Cards - {self.get_sim_cards_list()}"
    

computer = Computer("Intel Core i7", 16)
phone = Phone()
phone.set_sim_cards_list(["Beeline", "MegaCom"])
smartphone1 = SmartPhone("Apple A14 Bionic", 64)
smartphone1.set_sim_cards_list(["O!Mobile", "MegaCom"])
smartphone2 = SmartPhone("Samsung Exynos 2100", 128)
smartphone2.set_sim_cards_list(["Beeline", "O!Mobile"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer == smartphone1)
print(computer != smartphone2)
print(computer > smartphone1)
print(computer <= smartphone2)