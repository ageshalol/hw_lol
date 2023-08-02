#задача 1
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def info(self):
#         print(f"Brand: {self.brand}, model {self.model}")
    
# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model)
#         self.year = year
    
#     def info(self):
#         super().info()
#         print(f"Year: {self.year}")

# car = Car("Nissan", "Silvia s14", 2000)
# car.info()

#задача 2
class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Mother(Parent):
  def __init__(self, first_name, last_name, child_count):
    super().__init__(first_name, last_name)
    self.child_count = child_count

  def get_child_count(self):
    print(f"Mother: {self.child_count}")

class Father(Parent):
  def __init__(self, first_name, last_name, child_count):
    super().__init__(first_name, last_name)
    self.child_count = child_count

  def get_child_count(self):
    print(f"Father: {self.child_count}")

mother = Mother("Atabek", "lol", 3)
father = Father("Anelya", "lloll", 3)
mother.get_full_name()
mother.get_child_count()
father.get_full_name()
father.get_child_count()