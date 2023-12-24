
import functools
filepath = './input/CamelCards.txt'
scores = {}
hands = []
poker = 'AKQJT98765432'

# Create a mapping from char to index
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
    for card, count in sorted_count:
        if count == 5:
            return 0
        elif count == 4:
            return 1
        elif count == 3:
            for newcard, newcount in sorted_count:
                if newcount == 2:
                    return 2
            return 3
        elif count == 2:
            for newcard, newcount in sorted_count:
                if newcard != card and newcount == 2:
                    return 4
            return 5
        else:
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
total_score = sum((index + 1) * scores[card] for index, card in enumerate(hands))

print(total_score)
