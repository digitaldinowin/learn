class Student:
    def __init__(self, name): #constructor
        self.name = name

    def greeting(self, name):
        print(self.name + " says: 'Hello, " + name + ".'")
    
    def play(self, game):
        print(self.name + " is playing " + game.name)
        game.start()

    def pauseGame(self, game):
        print(self.name + ' paused the game')
        game.pause()


class Game:
    def __init__(self, name):
        self.name = name    

    def start(self):
        self.makeSound()
        self.terminate()

    def makeSound(self):
        print('some sound')   
    
    def terminate(self):
        print('game over')
    
    def pause(self):
        print('Game paused. Wish you back')


# s1 = Student("Luning")
# s1.greeting('Haoning')
# s1.greeting('Andy')