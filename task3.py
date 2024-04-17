import random

cards = {}
cards2 = []
cardranks = ["2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "Jack of ", "Queen of ", "King of ","Ace of "]
cardsuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
players = {
    "player1" : [],
    "player2" : [],
    "player3" : [],
    "player4" : []
    }
final = {
    "player1" : [],
    "player2" : [],
    "player3" : [],
    "player4" : []
    }

check = 0 
for x in cardsuits:
    for z in cardranks:
        cards[f"{z}{x}"] = check
        check = check + 1
#print(cards)

for x in cards:
    cards2.append(x)
#print(cards2)

random.shuffle(cards2)
#print(cards2)

for x in range(5):
    for z in players:
        players[f"{z}"].append(cards2[0])
        cards2.pop(0)
#print(cards2)

for x in players:
    for z in players[x]:
        print(z)
        print(cards[z])


    print("\n")

    

#for x in players:
    #print(players[x])