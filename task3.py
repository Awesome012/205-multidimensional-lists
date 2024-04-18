import random
from typing import Final

cards = {}
cardranks = ["2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "Jack of ", "Queen of ", "King of ","Ace of "]
cardsuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
players = {
    "player1" : {},
    "player2" : {},
    "player3" : {},
    "player4" : {}
    }

check = 0 
for x in cardsuits:
    for z in cardranks:
        cards[f"{z}{x}"] = check
        check = check + 1
#print(cards)

temp = list(cards.values())
random.shuffle(temp)
test = dict(zip(cards, temp))
final = dict(sorted(test.items(), key=lambda item: item[1]))
#print(final)

for x in final:
    #print(x)
    continue
cool = list(cards.keys())[0]
#print(cool)
#print(cards)
for x in range(5):
    for z in players:
        cool = list(final.keys())[0]
        nice = cards[cool]
        players[z][cool] = nice
        del final[cool]
        del cards[cool]
        players[z][cool] = nice
#print(players)
for x in players:
    #print(players[x])
    continue
#print(players)
players.sort()
#print(cards)

for x in players:
    for z in players[x]:
        print(z)
        continue


    print("\n")

#print(cards)


#for x in players:
    #print(players[x])