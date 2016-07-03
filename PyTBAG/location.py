'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''

class Location(object):
    '''
    classdocs
    '''


    def __init__(self, name, desc):
        '''
        Constructor
        '''
        self.name = name
        self.desc = desc
        self.exits = []
        self.people = []
        self.items = []
        
    def addExit(self, exit):
        self.exits.append(exit)
        
    def addPerson(self, person):
        self.people.append(person)
        
    def addItem(self, item):
        self.items.append(item)
        