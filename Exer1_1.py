# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:16:19 2019

@author: Daniella
"""
from random import shuffle 

suits = ['Clubs','Spades','Hearts','Diamonds']
val = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value       
    def show(self):
        return '{} of {}'.format(self.value,self.suit)
    
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in suits:
            for n in val:
                card = Card(s,n)
                self.cards.append(card)
    def show(self):
        for i in self.cards:
            print(i.show())   
    def deal(self):  #remove a card
            return self.cards.pop()
    def shuffle_deck(self):
        return shuffle(self.cards)
class Player:
    def __init__(self,name):
        self.name = name
        self.hand= []     
    def draw(self,D):
        D.shuffle_deck()
        self.hand.append(D.deal())
        return self
    def show_hand(self):
        for j in self.hand:
            print(j.show())
    
class Game(Player):
    def __init__(self,hand):
        self.hand=hand
        
    def facevalue(self):
        array= []
        for k in self.hand:
            card= k.value.split()
            if card[0] in ['A','J','Q','K']:
                face_value = 10
                array.append(face_value)
            elif card[0] in ['2','3','4','5','6','7','8','9','10']:
                face_value = int(card[0])
                array.append(face_value)
        return array
    
    def add(self,val_1,val_2):
        return val_1 + val_2
    def compete(self,p1,p2):
        if p1 > p2:
            print('Player 1' + ' ' + ' WINS')
        elif p1 == p2:
            print('DRAW! Pick 2 cards agin')
        else:
            print('Player 2' + ' ' + 'WINS')
        
    
deck = Deck() 
P_1= Player('Dani')
P_1.draw(deck)
P_1.draw(deck)      
r=P_1.hand
g=Game(r)
A=g.facevalue()
summ=g.add(A[0],A[1])
#print(summ)
print('Player 1:'+ P_1.name)
P_1.show_hand()

print('')
P_2= Player('Ollie')
P_2.draw(deck)
P_2.draw(deck)      
rr=P_2.hand
gg=Game(rr)
B=gg.facevalue()
summm = gg.add(B[0],B[1])
print('Player 2:' + P_2.name)
P_2.show_hand()

#GAME
print('')
g.compete(summ,summm)

        