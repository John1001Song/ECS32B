import random

class Pet:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
        self.voice = 'Hello World'

    def sound(self):
        print("This is pet default sound: ", self.voice)

    def __ssn(self):
        return random.random()

    def print_Pet(self):
        print('Pet name: ', self.name)
        print('Pet age: ', self.age)
        print('Pet type: ', self.type)
        print(self.__ssn())

    @staticmethod
    def calculate(a:int, b:int) -> int:
        print('a + b = ', a+b)


class Dog(Pet):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)
        self.voice = 'bow'

    def dog_sound(self):
        print("This is dog sound: ", self.voice)

    def default_sound(self):
        self.sound()

class Cat(Pet):
    def __init__(self):
        print('Cat is different.')

    def get_ssn(self):
        self.__ssn()

if __name__ == '__main__':
    p = Pet('JJ', 3, 'alien')
    p.sound()
    p.print_Pet()

    print("==========================")

    d = Dog('Doggy', '2', 'dog')
    d.sound()

    d.dog_sound()
    d.print_Pet()

    print("==========================")

    try:
        c = Cat()
        print(c.voice)
    except Exception as e:
        print('Error occurs: ', e)
    try:
        # c = Cat()
        # print(c.voice)
        c.get_ssn()
    except Exception as e:
        print('Error occurs: ', e)

    print("==========================")
    Pet.calculate(3, 5)
    d.calculate(2, 2)