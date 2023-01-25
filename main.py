import random

players = {}

class Player():
    @classmethod
    def create_desk(cls) -> list:
        nums = set()
        while len(nums) != 15:
            nums.add(random.randint(1, 90))
        nums = sorted(list(nums))
        for i in range(len(nums), 0, -5):
            for j in range(3):
                nums.insert(random.randint(i-5, i), "  ")
        nums.insert(8, "\n")
        nums.insert(17, "\n")
        return nums

    def __init__(self, name: str, desk):
        self.name = name
        self.desk = desk
    
    def __str__(self) -> str:
        return f"Никнейм игрока - {self.name}."
            
    def __eq__(self, __o: object) -> bool:
        return len(list(filter(lambda x: type(x) == int, self.desk))) == len(list(filter(lambda x: type(x) == int, __o.desk)))

    def print_desk(self):
        desk = f"Доска игрока '{self.name}':\n{'-'*25}\n"
        lst = self.desk
        for elem in lst:
            desk += " " + str(elem)
        desk += f"\n{'-'*25}"
        print(desk)

def create_player(name):
    players[name] = Player(name, Player.create_desk())



polling = True
if __name__ == "__main__":
    mode_choice = input("Режимы игры:\n1. Человек - компьютер\n2. Человек - человек\n3. Компьютер - компьютер\nВведите выбранную опцию: ")
    if mode_choice == "2":
        for i in range(int(input("Начнем игру! Введите количество игроков: "))):    
            create_player(input(f"Игрок №{i+1}, введите ваш Ник: "))
    elif mode_choice == "1":
        create_player(input(f"Введите ваш Ник: "))
        create_player("Компьютер")
    elif mode_choice == "3":
        create_player("Макбук")
        create_player("ХП на Дебиан")
    else:
        print("Такого варианта не было, до свидания!")
        polling = False
    
    while polling == True:
        for val in players.values():            
            filtred = list(filter(lambda x: type(x) == int, val.desk))
            val.print_desk()
            if not filtred:
                print(f"Игрок {val.name} победил!!!")
                polling = False
                continue
        bochonok = random.randint(1, 90)
        print(f"Новый бочонок! Номер {bochonok}!")
        for chel in players.values():
            if chel.name == "Проигравший!":
                continue
            if chel.name == "Компьютер" or chel.name == "Макбук" or chel.name == "ХП на Дебиан":
                if bochonok in chel.desk:
                    index = chel.desk.index(bochonok)
                    chel.desk[index] = "-"
            else:
                choice = input('На вашей карточке есть такая цифра? (Y/N): ').lower()
                if choice == "y" and bochonok in chel.desk:
                    index = chel.desk.index(bochonok)
                    chel.desk[index] = "-"
                elif choice == 'y' and bochonok not in chel.desk:
                    print("Вы проиграли! Будьте внимательнее!")
                    chel.name = "Проигравший!"
                    chel.desk = [0, "Лузер  лузеР", 0]
                elif choice == "n" and bochonok in chel.desk:
                    print("Вы проиграли! Будьте внимательнее!")
                    chel.name = "Проигравший!"
                    chel.desk = [0, "Лузер  лузеР", 0]
                elif choice == 'n' and bochonok not in chel.desk:
                    continue
                else:
                    print("Кажется я не понял что вы ответили... Пожалуйста, выржайтесь яснее в следующий раз!")
