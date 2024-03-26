class Dog:
    _legs = 4
    def _innit__(self, name):
        self.name = name

    def __init__(self):
        print (self.name + "says : Bark!")

    def __init__(self):
        return self._legs

class Chihuahua(Dog):
    def speak(self):
        print (f'{self.name} says : Yap Yap Yap!')

    def wagtail(self):
        print ('Vigorous Wagging')
