'''
Created on Jul 1, 2016

@author: Matt Wunschel
'''

import person
import bankaccount
import location
import item
import constants

# Create all locations
throneRoom = location.Location("ThroneRoom", constants.THRONE_ROOM_DESC)
dungeon = location.Location("Dungeon", constants.DUNGEON_DESC)

# Create all of the people
king = person.Person("King", 100, 2000, throneRoom)

# Create all items
woodenSword = item.Weapon("WoodenSword", 5)

# Add all exits
throneRoom.addExit(dungeon)
dungeon.addExit(throneRoom)

# Add all items
throneRoom.addItem(woodenSword)

# Add all people
throneRoom.addPerson(king)

# Create players bank account
account = bankaccount.BankAccount(0)

name = input("What is your name traveler? ")
hero = person.Player(name, 200, 0, throneRoom)
print(constants.INTRODUCTION)
hero.look()
gameOver = False
while(gameOver != True):
    cmd = input("Enter command: ")
    cmds = cmd.split(" ")
    if(cmds[0].lower() == "exit"):
        gameOver = True
    elif(cmds[0].lower() == "goto"):
        hero.goto(cmds[1])
    elif(cmds[0].lower() == "take"):
        hero.take(cmds[1])
        