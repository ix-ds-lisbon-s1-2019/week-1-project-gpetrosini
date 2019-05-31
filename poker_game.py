#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:53:20 2019

@author: gracepetrosini
"""
#%%
import sys
import random

playeramount = int(sys.argv[1])

print(playeramount)

class PokerGame:
    
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players #this is a class attribute
        self.namelist = []
        self.hand = []
        
    def names(self):
        for i in range(self.number_of_players):
            self.namelist.append(input("What is your name?"))
        print(self.namelist)

    def dealer(self):
        self.card_choices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.playerHands = {}
        self.winnerList = self.namelist.copy()
        z = 0
        for player in self.namelist:
            self.hand = []
            for value in range(5):
                self.hand.append(random.choice(self.card_choices))
                self.hand.sort(reverse = True)
            print(player + ": " + " ".join(str(self.hand)))
            self.playerHands[player] = self.hand
        #print(self.playerHands)
        while (z<5) and (len(self.winnerList)>1):
            max = 1
            for i in self.winnerList:
                if self.playerHands[i][z] > max:
                    self.winnerList = [i]
                    max = self.playerHands[i][z]
                if self.playerHands[i][z] == max:
                    if i not in self.winnerList:
                        self.winnerList.append(i)
            z += 1
            
        print("Winner is " + "".join(str(self.winnerList)))
                
                    

game1 = PokerGame(playeramount)
game1.names()
game1.dealer()

