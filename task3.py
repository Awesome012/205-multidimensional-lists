import random

cards = []
cardranks = ["2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "Jack of ", "Queen of ", "King of ","Ace of "]
cardsuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
players = {
    "player1" : {},
    "player2" : {},
    "player3" : {},
    "player4" : {}
    }

for x in cardsuits:
    for z in cardranks:
        cards.append(f"{z}{x}")

random.shuffle(cards)
print(cards)

for x in range(5):
    for z in players:
        check = players.index('player1')
        players[f'{x}'].append("0")

print(players)