from enum import Enum
from functools import cmp_to_key


class HandType(Enum):
    FIVEKIND = 6
    FOURKIND = 5
    FULLHOUSE = 4
    THREEKIND = 3
    TWOPAIR = 2
    ONEPAIR = 1
    HIGHCARD = 0




def main():
    filename = "input.txt"
    #filename = "test.txt"

    with open(filename, "r") as file:
        inputRead = file.readlines()


    hands = []

    for line in inputRead:
        hand, bet = line.split()
        hands.append((hand, int(bet)))

    ranked_hands= sorted(hands, key= cmp_to_key(compareTwoHands))

    total_part1 = 0
    for rank, hand_bet in enumerate(ranked_hands):
        bet = hand_bet[1]
        rank += 1
        total_part1 += bet * rank


    print("part1:", total_part1)

        




def compareTwoHands(first, second):
    """ return 1 if the first is higher, -1 if its the second 
    (0 if they were equal which should never be the case with the given input)"""

    first_hand = first[0]
    second_hand = second[0]

    first_type = getHandType(first_hand)
    second_type = getHandType(second_hand)

    if first_type.value > second_type.value:
        return 1
    
    if second_type.value > first_type.value:
        return -1


    cards_strength = {
        "2" : 0,
        "3" : 1,
        "4" : 2,
        "5" : 3,
        "6" : 4,
        "7" : 5,
        "8" : 6,
        "9" : 7,
        
        "T" : 8,
        "J" : 9,
        "Q" : 10,
        "K" : 11,
        "A": 12
    }

    for i in range(len(first_hand)):
        if cards_strength[first_hand[i]] > cards_strength[second_hand[i]]:
            return 1
        if cards_strength[first_hand[i]] < cards_strength[second_hand[i]]:
            return -1

    return 0



def getHandType(hand):
    distinct_cards = list(set(hand))
    number_of_distinct_cards = len(distinct_cards)

    if number_of_distinct_cards == 1:
        return HandType.FIVEKIND

    if number_of_distinct_cards == 2:
        if hand.count(distinct_cards[0]) == 4 or hand.count(distinct_cards[0]) == 1:
            return HandType.FOURKIND 
        return HandType.FULLHOUSE

    if number_of_distinct_cards == 3:
        if any(hand.count(n) == 3 for n in hand):
            return HandType.THREEKIND
        return  HandType.TWOPAIR

    if number_of_distinct_cards == 4:
        return HandType.ONEPAIR

    return HandType.HIGHCARD


    





if __name__ == "__main__":
    main()