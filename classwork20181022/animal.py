import abc

class Animal:
    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def voice(self):
        print('dasd')

a = Animal()
a.voice()

class Bird(Animal):
    def voice(self):
        print('chik-chirik')

Bird().voice()