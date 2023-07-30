class SlotMachine:
    def __init__(self, name):
        self.name = name
        self.user_balance = 100
        self.game_balance = 0

    def info(self):
        print("Player:", self.name)
        print("User balance:", self.user_balance)
        print("Game balance:", self.game_balance)

    def top_up_balance(self, amount):
        if amount <= 100:
            self.balance_up(amount)
        else:
            print("Вы можете пополнить до 100$")

    def balance_up(self, amount):
        self.user_balance -= amount
        self.game_balance += amount

    def game(self):
        import random
        secret_number = random.randint(1, 10)
        attempts = 5

        while attempts > 0:
            guess = int(input("Угадайте число от 1 до 10: "))
            if guess == secret_number:
                print("Вы выиграли!")
                self.game_balance += 50
                return
            else:
                print("Вы не угадали.")
                self.user_balance -= 10
                attempts -= 1

        print("Вы проиграли.")

    def conclusion_money(self, amount):
        if amount >= 50:
            self.balance_up(amount)
        else:
            print("Вывести можно от 50$")

    def main(self):
        command = input("Введите команду (1, 2, 3 или 4): ")
        if command == "1":
            self.info()
        elif command == "2":
            amount = int(input("Введите сумму для пополнения игрового баланса: "))
            self.top_up_balance(amount)
        elif command == "3":
            self.game()
        elif command == "4":
            amount = int(input("Введите сумму для вывода из игрового баланса: "))
            self.conclusion_money(amount)
        else:
            print("Недопустимая команда.")


slot_machine = SlotMachine("Player 1")
slot_machine.main()