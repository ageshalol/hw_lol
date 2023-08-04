#заача 1
# class Shape:
#     def draw(self):
#         return f"Рисуем фигуру"
        
# class Circle(Shape):
#     def draw(self):
#         return f"Рисуем круг"
    
# class Rectangle(Shape):
#     def draw(self):
#         return f"Рисуем Прямоугольник"

# shape = Shape()
# circle = Circle()
# rectangle = Rectangle()

# print(shape.draw())  
# print(circle.draw())  
# print(rectangle.draw())  

#задача 2
class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self, value):
        self.value += value
    
    def get_value(self):
        return self.value
    
counter = Counter()
print(counter.get_value())  
counter.increment(30)
print(counter.get_value()) 
counter.increment(60)
print(counter.get_value())  