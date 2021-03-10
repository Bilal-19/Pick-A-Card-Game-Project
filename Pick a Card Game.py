# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:47:54 2021

@author: LENOVO
"""

import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value
        print(f"{val} of {self.suit}")


class Deck(object):
    def __init__(self):
        self.build()

    def show(self):
        '''This function display all cards in the deck'''
        for card in self.cards:
            print(card,end=",")

    def build(self):
        '''This function generate 52 cards'''
        self.cards = []
        Suit  = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        for suits in Suit:
            for val in range(1,14):
                self.cards.append(suits)
                self.cards.append(val)
        return self.cards

    def shuffle(self):
        '''This function shuffle the deck'''
        for i in range(1):
            for i in range(len(self.cards)-1, 0, -1):
                y = random.randint(0, i)
                if i == y:
                    continue
                self.cards[i], self.cards[y] = self.cards[y], self.cards[i]
        return self.cards

    def deal(self):
        '''This function return the top card'''
        return self.cards.pop()
    
    def Valid(self,deck):
        for i in range(len(self.cards)):
            if self.cards[i] == deck:
                return True
        return False

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print("Hi!, My Name is",self.name)

    def draw(self,deck):
        self.hand.append(deck)

    def showHand(self):
        print(f"{self.name}'s hand: {self.hand}")

    def discard(self):
        return self.hand.pop()
        
name = input("Enter Your Name: ")
Player1 = Player(name)
Player1.sayHello()

CardDeck = Deck()
print("\t\t\tCard Deck:\n",CardDeck.build())
print("\n\n\t\tAfter Shuffling the Card Deck:\n",CardDeck.shuffle())
print("\nTop Card in Card Deck is:",CardDeck.deal())

print("\nLet us draw the deck")
deck = input("Enter the deck which you want to draw: ")
Player1.draw(deck)
Player1.showHand()
print(Player1.discard())
