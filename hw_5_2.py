#задача 1 инкапсуляция
class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
    
    def bark(self):
        print(f"{self._name} лает: Гав-гав!")
    
    def get_breed(self):
        return self._breed
    

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    def meow(self):
        print(f"{self._name} мяукает: Мяу-мяу!")
    
    def get_color(self):
        return self._color