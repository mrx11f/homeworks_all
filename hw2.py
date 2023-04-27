class Figure:
    unit = 'cm'  # или 'mm', единица измерения по умолчанию

    def calculate_area(self):
        pass

    def info(self):
        pass
    
class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius


    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_a * self.__side_b / 2
    
    def info(self):
        print(f"square: {self.calculate_area():.2f}{self.unit}") 

    def info(self):
        print(f"RightTriangle side a: {self.a}{self.unit}, side b: {self.b}{self.unit}, area: {self.calculate_area()}{self.unit}")

figures = [
    Circle(3),        
    Circle(5),        
    RightTriangle(3, 4), 
    RightTriangle(4, 4), 
    RightTriangle(2, 6) 
]

for figure in figures:
    figure.info()