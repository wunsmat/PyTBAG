'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''

import item

class Crafting(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def combineWeapons(self, wpn1, wpn2):
        attack = wpn1.attack + wpn2.attack
        return item.Weapon(attack)