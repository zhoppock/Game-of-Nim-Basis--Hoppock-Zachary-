import random
pileSize = int(random.randint(10, 100))
print("The amount of marbles will be " + str(pileSize) + ".\n")
pileHalf = int(pileSize/2)


print(" > The first player to get to the last marble wins. < \n")
first = random.randint(0, 1)
print("0 is for Player 1.  1 is for Player 2.  Who goes first:", first, "\n")

if first == 0:
  player = 1
  print("Player 1 goes first! \n")
elif first == 1:
  player = 2
  print("Player 2 goes first! \n")

while True:
  if player == 1:
    print(" > Player", player, "<")
    while True:
      take = int(input("How many marbles will you take out of " + str(pileHalf) + "? \n"))
      if take <= pileHalf and take > 0:
        break
      else:
        print("Illegal move")
  if player == 2:
    print(" > Player", player, "<")
    while True:
      print("How many marbles will you take out of " + str(pileHalf) + "?")
      take = int(random.uniform(1, pileHalf))
      print(take)
      break
        
    
  pileSize = int(pileSize - take)
  pileHalf = int(pileSize/2)

  print("The amount of marbles is now " + str(pileSize) + ". \n")

  if pileSize < 2:
    print("\n Player", player, "wins!")
    break
  if player == 1:
    player = 2
  else:
    player = 1