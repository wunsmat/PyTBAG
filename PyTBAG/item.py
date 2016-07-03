'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''
class Item(object):
    '''
    Items are objects that the player class can pickup and use
    '''
    def ___init__(self, name):
        self.name = name
    
class Weapon(Item):
    '''
    classdocs
    '''


    def __init__(self, name, attack):
        super(self.__class__, self).___init__(name)
        '''
        Constructor
        '''
        self.attack = attack
        