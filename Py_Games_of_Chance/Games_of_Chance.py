import random

money = 100

#Write your game of chance functions here


def coinflip(call,bet):
  num=random.randint(1,2)
  if num==2:
    flip="Heads"
  else:
    flip="Tails"
  if call==flip:
    return("You won:"+str(bet))
  else:
    return("You won:-"+str(bet))

def cho_han(call,bet):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  if ((dice1+dice2)%2)==0:
    outcome="Even"
  else:
    outcome="Odd"
  if call==outcome:
    return("You won:"+str(bet))
  else:
    return("You won:-"+str(bet))

def cardpick(call,bet):
  card1=random.randint(1,13)
  card2=random.randint(1,13)
  if card1>card2:
    outcome="Higher"
  elif card2<card1:
    outcome="Lower"
  else:
    outcome="Even"
  if call==outcome:
    return("You won:"+str(bet))
  else:
    return("You won:-"+str(bet))
  
#Call your game of chance functions here
print(coinflip("Heads",20))
print(cho_han("Odd",20))
print(cardpick("Higher",50))
