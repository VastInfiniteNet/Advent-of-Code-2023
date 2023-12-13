from functools import cmp_to_key

def part1():
   total = 0
   highCard, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind = [], [], [], [], [], [], []
   cardValue = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
   ranks = [highCard, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind]
   f = open('day07/day07.txt')
   for line in f:
      hand, bid = line.strip().split()
      cards = list(hand)
      counts: list = [hand.count(card) for card in set(cards)]
      counts.sort(reverse=True)
      pair = (hand, bid)
      match counts:
         case [5]:
            fiveKind.append(pair)
         case [4, _]:
            fourKind.append(pair)
         case [3, 2]:
            fullHouse.append(pair)
         case [3, *rest]:
            threeKind.append(pair)
         case [2, 2, *rest]:
            twoPair.append(pair)
         case [2, *rest]:
            onePair.append(pair)
         case _:
            highCard.append(pair)
   
   def compareHandFunc(a, b):
      for i in range(0,len(a[0])):
         cardDiff = cardValue[a[0][i]] - cardValue[b[0][i]]
         if cardDiff == 0:
            continue
         return cardDiff
      return 1
   
   allRanks = []
   for rank in ranks: # order each rank
      rank.sort(key=cmp_to_key(compareHandFunc))
      allRanks += rank

   # score
   for i in range(len(allRanks)):
      total += (i + 1) * int(allRanks[i][1])
   
   f.close()
   return total


def part2():
   total, joker = 0, "J"
   highCard, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind = [], [], [], [], [], [], []
   cardValue = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 0, 'Q': 11, 'K': 12, 'A': 13}
   ranks = [highCard, onePair, twoPair, threeKind, fullHouse, fourKind, fiveKind]
   f = open('day07/day07.txt')
   def compareCardCounts(a, b):
      val = a[0] - b[0] # compare card counts in hand
      if val == 0: # compare card value in hand 
         return cardValue[a[1]] - cardValue[b[1]]
      return val
   
   for line in f:
      hand, bid = line.strip().split()
      cards = list(hand)
      counts: list = [(hand.count(card), card) for card in set(cards) if card != joker]
      jokerCount = hand.count(joker)
      counts.sort(reverse=True, key=cmp_to_key(compareCardCounts))
      if jokerCount == 5:
         counts = [(0, joker)]
      counts[0] = (counts[0][0] + jokerCount, counts[0][1])
      
      pair = (hand, bid)
      match counts:
         case [(5, _)]:
            fiveKind.append(pair)
         case [(4,_), _]:
            fourKind.append(pair)
         case [(3, _), (2, _)]:
            fullHouse.append(pair)
         case [(3, _), *rest]:
            threeKind.append(pair)
         case [(2, _), (2, _), *rest]:
            twoPair.append(pair)
         case [(2, _), *rest]:
            onePair.append(pair)
         case _:
            highCard.append(pair)
   
   def compareHandFunc(a, b):
      for i in range(len(a[0])):
         cardDiff = cardValue[a[0][i]] - cardValue[b[0][i]]
         if cardDiff == 0:
            continue
         return cardDiff
      return 1
   
   allRanks = []
   for rank in ranks: # order each rank
      rank.sort(key=cmp_to_key(compareHandFunc))
      allRanks += rank
      
   # score
   for i in range(len(allRanks)):
      total += (i + 1) * int(allRanks[i][1])
   
   f.close()
   return total


print(part2())