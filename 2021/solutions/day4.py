#!/usr/bin/env python3

import os
import sys

"""
"Zhu Li, do the thing!"
"Yes Varrick"
"""
def pythonDoTheThing(input_file):
    with open(input_file,'r') as f:
        lines = f.readlines()
    
    # Take the input file and organize it into the list of bingo cards and the deck of numbers for the announcer to draw from
    number_deck, bingo_cards = lines[0].split(','), []
    for i in range(1, len(lines), 6):
        bingo_card = []
        for k in range(1,6):
            bingo_card.append(lines[i+k].strip().split())
        bingo_cards.append(bingo_card)

    score = playBingo(number_deck, bingo_cards)
    #print("Answer = %d" % (score))

"""
Draw a number from the deck and mark each card, and the game ends when a winning card is found
"""
def playBingo(deck, card_list):

    winners = []
    winningNum = 0
    # Announcer draws a number
    for turn, number in enumerate(deck):

        # Check each bingo card
        for card_num, card in enumerate(card_list):
            if card_num not in winners: # for part 2, we want to find the last player to win (which was card #71)
                markCard(number, card) # mark the card
                if bingo(card): # check if the card won
                    winners.append(card_num)
                    winningNum = int(number)
    
    print(calculateCardScore(card_list[winners[-1]]) * int(winningNum)) 

"""
Provided a number and a bingo card, if the number exists on the card, replace it with a mark 'M'
"""
def markCard(num, bingo_card):
    # Check each row for the number and replace it with an 'M' if found
    for row in bingo_card:
        if row.count(num) > 0:
            row[row.index(num)] = 'M'

"""
Check a bingo_card to see if it won
"""
def bingo(bingo_card): 
    
    for row in range(5):
        # count the whole row for the number of 'M' marks
        if bingo_card[row].count('M') == 5:
            return True
       
        # check the whole column
        won = True
        for col in range(5):
            if bingo_card[col][row] != 'M':
                won = False
        
        if won:
            return True

    # If we didn't find a winning row or col, we don't have bingo
    return False
        
"""
Once a winner is found, count up all non-marked numbers and return the score
"""
def calculateCardScore(bingo_card):
    score = 0
    for row in bingo_card:
        for num in row:
            if num != 'M':
                score += int(num)

    return score

def main(arguments):
    input_file = "input" + arguments[0][3:arguments[0].index('.')] + ".txt"
    pythonDoTheThing(input_file)

if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
