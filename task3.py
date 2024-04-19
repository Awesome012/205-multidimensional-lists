import random
from typing import Final

cards = {}
cardranks = ["2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "Jack of ", "Queen of ", "King of ","Ace of "]
cardsuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
players = {
    "Player 1" : {},
    "Player 2" : {},
    "Player 3" : {},
    "Player 4" : {}
    }

check = 0 
for x in cardsuits:
    for z in cardranks:
        cards[f"{z}{x}"] = check
        check = check + 1

temp = list(cards.values())
random.shuffle(temp)
test = dict(zip(cards, temp))
final = dict(sorted(test.items(), key=lambda item: item[1]))
cool = list(cards.keys())[0]

for x in range(5):
    for z in players:
        cool = list(final.keys())[0]
        nice = cards[cool]
        players[z][cool] = nice
        del final[cool]
        del cards[cool]
        players[z][cool] = nice

for x in players:
    players[x] = sorted(players[x].items(), key=lambda x:x[1])
    players[x] = dict(players[x])


for x in players:
    print(f"{x}:")
    for z in players[x]:
        print(z)
        continue
    print("")