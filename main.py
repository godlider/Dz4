import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp Chirp"

    def eat(self):
        return "Seeds"

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Roar"

    def eat(self):
        return "Grass"

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Hiss"

    def eat(self):
        return "Insects"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_zoo(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_zoo(file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)

# Класс ZooKeeper
class ZooKeeper:
    def feed_animal(self, animal):
        return f"Feeding {animal.name}"

# Класс Veterinarian
class Veterinarian:
    def heal_animal(self, animal):
        return f"Healing {animal.name}"

# Пример использования классов
bird = Bird("Parrot", 5, "Green")
mammal = Mammal("Lion", 8, "Golden")
reptile = Reptile("Snake", 3, "Black")

animals = [bird, mammal, reptile]
animal_sound(animals)

zoo = Zoo()
zoo_keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

# Сохранение информации о зоопарке в файл
zoo.save_zoo('zoo.pkl')

# Загрузка информации о зоопарке из файла
loaded_zoo = Zoo.load_zoo('zoo.pkl')

print(loaded_zoo)