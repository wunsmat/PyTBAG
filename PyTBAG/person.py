'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''

class Person(object):
    '''
    The Person class are for NPCs
    '''

    def __init__(self, name, hp, gold, location):
        '''
        Constructor
        '''
        self.name = name
        self.hp = hp
        self.gold = gold
        self.alive = True
        self.location = location
        
class Player(Person):
    '''
    The Player class is a Person that the user controls
    '''
    def __init__(self, name, hp, gold, location):
        super(self.__class__, self).__init__(name, hp, gold, location)
        '''
        Constructor
        '''
        self.inventory = []
    
    def goto(self, exitName):
        found = False
        print("----------------------------------------------")
        for place in self.location.exits:
            if(place.name.lower() == exitName.lower()):
                self.location = place
                print("You have successfully went to " + exitName)
                self.look()
                found = True
            if(found != True):
                print("You could not go to " + exitName)
        print("----------------------------------------------")
                
    def look(self):
        print(self.location.desc)
        if(len(self.location.exits) > 0):
            print("You see the following exits:")
            for x in self.location.exits:
                print(x.name)
        if(len(self.location.items) > 0):
            print("You see the following items:")
            for x in self.location.items:
                print(x.name)
    
    def take(self, itemName):
        found = False
        print("----------------------------------------------")
        for item in self.location.items:
            if(item.name.lower() == itemName.lower()):
                self.inventory.append(item)
                self.location.items.remove(item)
                print("You have successfully picked up " + itemName)
                self.look()
                found = True
            if(found != True):
                print("You could not pick up " + itemName)            
        print("----------------------------------------------")