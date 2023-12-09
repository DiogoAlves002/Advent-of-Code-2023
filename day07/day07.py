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
        getBestPossibleHandType(hand)

    ranked_hands= sorted(hands, key= cmp_to_key(compareTwoHands))
    ranked_with_joker_hands= sorted(hands, key= cmp_to_key(compareTwoHandsWithJoker))

    total_part1 = 0
    total_part2 = 0
    """ for rank, hand_bet in enumerate(ranked_hands):
        bet = hand_bet[1]
        rank += 1
        total_part1 += bet * rank """

    for rank in range(len(hands)):
        bet_normal = ranked_hands[rank][1]
        bet_with_joker = ranked_with_joker_hands[rank][1]

        rank += 1

        total_part1 += bet_normal * rank
        total_part2 += bet_with_joker * rank



    print("part1:", total_part1)
    print("part2:", total_part2)

        




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


def compareTwoHandsWithJoker(first, second):
    """ 
        return 1 if the first is higher, -1 if its the second 
        (0 if they were equal which should never be the case with the input given) \n
        this is exactly the same as the original function but with different card strength,
        cmp_to_key() doesn't seem to accept functions with more than 2 inputs so I can't just use one for both cases
    """ 

    first_hand = first[0]
    second_hand = second[0]

    first_type = getBestPossibleHandType(first_hand)
    second_type = getBestPossibleHandType(second_hand)

    if first_type.value > second_type.value:
        return 1
    
    if second_type.value > first_type.value:
        return -1


    cards_strength = {
        "J" : 0,

        "2" : 1,
        "3" : 2,
        "4" : 3,
        "5" : 4,
        "6" : 5,
        "7" : 6,
        "8" : 7,
        "9" : 8,
        
        "T" : 9,
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
        if hand.count(distinct_cards[0]) == 4 or hand.count(distinct_cards[1]) == 4:
            return HandType.FOURKIND 
        return HandType.FULLHOUSE

    if number_of_distinct_cards == 3:
        if any(hand.count(n) == 3 for n in hand):
            return HandType.THREEKIND
        return  HandType.TWOPAIR

    if number_of_distinct_cards == 4:
        return HandType.ONEPAIR

    return HandType.HIGHCARD


def getBestPossibleHandType(hand):

    number_of_jokers = hand.count("J")
    if number_of_jokers == 0:
        return getHandType(hand)

    distinct_cards_without_joker = list(set(hand))
    distinct_cards_without_joker.remove("J")

    number_of_distinct_cards_without_joker = len(distinct_cards_without_joker)

    # NOTE: this is a bit of a mess, it could probably be refactored

    if number_of_jokers == 5 or number_of_distinct_cards_without_joker == 1:
        return HandType.FIVEKIND

    if number_of_distinct_cards_without_joker == 2:
        if (hand.count(distinct_cards_without_joker[0]) + number_of_jokers == 4 or
            hand.count(distinct_cards_without_joker[1]) + number_of_jokers == 4):
            return HandType.FOURKIND

        if (hand.count(distinct_cards_without_joker[0]) == 1 and
            hand.count(distinct_cards_without_joker[1]) == 1):
            return HandType.FULLHOUSE
        
        if hand.count(distinct_cards_without_joker[0]) == 2:
            return HandType.FULLHOUSE

        return HandType.THREEKIND

    if number_of_distinct_cards_without_joker == 3: 
        if any(hand.count(card) + number_of_jokers == 3 for card in distinct_cards_without_joker):
            return HandType.THREEKIND
        return HandType.TWOPAIR

    return HandType.ONEPAIR
    

        


        

    





if __name__ == "__main__":
    main()