
import functools
filepath = './input/CamelCards.txt'
scores = {}
hands = []
poker = 'AKQT98765432J'

# Create a mapping from char to index plus 1
poker_mapping = {char: index for index, char in enumerate(poker)}

with open(filepath, 'r') as file:
    for line in file:
        parts = line.split()
        key = parts[0]
        value = int(parts[1])
        scores[key] = value
        hands.append(key)

def order(hand):
    count = {}
    for card in hand:
        count[card] = count.get(card, 0) + 1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    count_j = count.get('J', 0)
    '''
        J can represent any card
        0 same five cards
        1 same four cards and another one
        2 full house: same three cards and a pair
        3 same three cards and two different cards
        4 two group of same two cards and another one
        5 one group of same two cards and another three different one
        6 all different cards
    '''
    for card, count in sorted_count:
        if count == 5:
            return 0
        elif count == 4:
            if card == 'J' or count_j == 1: return 0
            return 1
        elif count == 3:
            if card == 'J':
                for newcard, newcount in sorted_count:
                    if newcount == 2:
                        return 0
                return 1
            if count_j == 2: return 0
            if count_j == 1: return 1
            for newcard, newcount in sorted_count:
                if newcount == 2:
                    return 2
            return 3
        elif count == 2:
            if card == 'J':
                for newcard, newcount in sorted_count:
                    if newcard != card and newcount == 2:
                        return 1
                return 3
            if count_j == 2:
                return 1
            if count_j == 1:
                for newcard, newcount in sorted_count:
                    if newcard != card and newcount == 2:
                        return 2 
                return 3
            for newcard, newcount in sorted_count:
                if newcard != card and newcount == 2:
                    return 4
            return 5
        else:
            if count_j == 1:
                return 5
            return 6
    return None
    
def compare_hands(handone, handtwo):

    orderone = order(handone)
    ordertwo = order(handtwo)
    if orderone < ordertwo:
        return -1
    elif orderone > ordertwo:
        return 1
    else:
        for cardone, cardtwo in zip(handone, handtwo):
            if poker_mapping[cardone] < poker_mapping[cardtwo]:
                return -1
            elif poker_mapping[cardone] > poker_mapping[cardtwo]:
                return 1
    return None

# Use the compare_strings function in the sort function
hands = sorted(hands, key=functools.cmp_to_key(compare_hands), reverse=True)
# Sum the sorted hands by each element's index + 1 times its score[element]
#total_score = sum((index + 1) * scores[card] for index, card in enumerate(hands))
total_score = 0
for index, card in enumerate(hands):
    total_score += (index + 1) * scores[card]
    print(card, total_score)
print(total_score)
