import sqlite3

connect = sqlite3.connect('standart.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS bank (
    name VARCHAR(100),
    surname VARCHAR(100),
    age INTEGER,
    balance INTEGER,
    wallet_id VARCHAR(50),
    email VARCHAR(255),
    password VARCHAR(100)
);
""")

class Bank:
    def __init__(self):
        self.name = None 
        self.surname = None 
        self.age = None 
        self.balance = None 
        self.wallet_id = None 
        self.email = None 

    def register(self, name, surname, age, email, password):
        # cursor = connect.cursor()
        # random_wallet_id = sqlite3.randint(11111111, 99999999)
        cursor.execute(f"""INSERT INTO bank (name, surname, age, balance, wallet_id, email, password) 
                       VALUES ('{name}', '{surname}', {age}, 0, '{92930192}', '{email}', '{password}');""")
        cursor.connection.commit()
        print(f"Уважаемый {name} {surname} вы успешно создали счет в нашем банке")

    def main(self):
        while True:
            command = input("1 - регистрация, 2 - информация, 3 - пополнить, 4 - вывести, 5 - выйти: ")
            if command == "1":
                name = input("введите Имя: ")
                surname = input("введите Фамилию: ")
                age = int(input("Возраст: "))
                email = input("Почта: ")
                password = input("Введите пароль: ")
                self.register(name, surname, age, email, password)
            elif command == "2":
                email = input("Почта: ")
                password = input("Пароль: ")
                self.authorization(email, password)
            elif command == "2":
                self.get_info()
            elif command == "4":
                amount = int(input("Сколько: "))
                self.top_up_balance(amount)
            elif command == "3":
                wallet_id = input('ID счета: ')
                amount = int(input("KGS: "))
                self.money_transfer(wallet_id, amount)

optima = Bank()
optima.main()



import sqlite3

connect = sqlite3.connect('bank.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
    name VARCHAR(100),
    surname VARCHAR(100),
    age INTEGER,
    balance INTEGER,
    wallet_id VARCHAR(50),
    email VARCHAR(255)
);
""")

class Bank:

    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.balance = 0
        self.wallet_id = None
        self.email = None

    def register(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        cursor = connect.cursor()
        cursor.execute(f"""INSERT INTO clients (name, surname, age, balance, wallet_id, email) 
                       VALUES ('{name}', '{surname}', {age}, 0, 'qwerty', '{email}');""")
        connect.commit()
        print(f"Уважаемый {name} {surname}, вы успешно создали счет в нашем банке")

    def deposit(self, amount):
        cursor = connect.cursor()
        cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}'")
        connect.commit()
        self.balance += amount


    def get_balance(self):
        print(f"Баланс на счете {self.name} {self.surname}: {self.balance}")

    def main(self):
        while True:
            command = input("1 - регистрация, 3 - информация, 4 - пополнить, 5 - вывести, 6 - выход: ")
            if command == "1":
                name = input("Имя: ")
                surname = input("Фамилия: ")
                age = int(input("Возраст: "))
                email = input("Почта: ")
                self.register(name, surname, age, email)
            elif command == "3":
                if self.email:
                    self.get_balance()
                else:
                    print("Вы не авторизованы")
            elif command == "4":
                if self.email:
                    amount = int(input("Введите сумму для пополнения: "))
                    self.deposit(amount)
                else:
                    print("Вы не авторизованы")

optima = Bank()
optima.main()