class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow"
class Bird(Animal):
    def speak(self):
        return "Tweet tweet!"
def main():
        dog = Dog("Buddy")
        cat = Cat("Mittens")
        bird = Bird("Polly")
        
        print(dog.name + ": " + dog.speak())
        print(cat.name + ": " + cat.speak())
        print(bird.name + ": " + bird.speak())
if __name__ == "__main__":
    main()