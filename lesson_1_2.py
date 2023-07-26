# class Geeks:
#     def summ(num1, num2):
#         return num1 + num2 
    
# geeks = Geeks()
# print(geeks.summ(2,5))

# class Nurbolot:
#     def summ(num1, num2):
#         return num1 - num2
    
#     def summ(num1, num2):
#         return num1 * num2
    
#     def summ(num1, num2):
#         return  num1 / num2
    
# nurbolot = Nurbolot
# print(nurbolot.summ(100,50))
# print(nurbolot.summ(1000,50))
# print(nurbolot.summ(1000,10))


class Students:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        print(f"Здраствуйте {self.name} {self.surname}. Ваша группа {self.group}")
        
students = Students("nurbolot", "lol", "10")
