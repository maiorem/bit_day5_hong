import random


class Player:
    def __init__(self,n):
        self.name = n
        self.position = 0


class Dice :

    def __init__(self):
        pass

    def roll(self):
        return random.randrange(1,7)


class Tile:

    def __init__(self):
        pass

class GameBoard:

    def __init__(self):
        pass





class GameUI:
    def __init__(self):
        pass

    def makePlayer(self):
        player_count = int(input("How many Players? : "))

        for x in range(player_count):
            input("What is player name? : ")