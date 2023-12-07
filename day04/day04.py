def part1():
   total = 0
   with open("day04/day04.txt") as f:
      for line in f:
         winNums, haveNums = line.split(':')[1].strip().split('|')
         winNums, haveNums = set(winNums.strip().split()), set(haveNums.strip().split())
         total += int(2 ** (len(haveNums.intersection(winNums)) - 1))
   
   return total

def part2():
   total = 0
   matchHistory = []
   with open("day04/day04.txt") as f:
      for line in f:
         winNums, haveNums = line.split(':')[1].strip().split('|')
         matchingCount = len(set(winNums.strip().split()).intersection(set(haveNums.strip().split())))
         matchHistory.append((1, matchingCount))

   while matchHistory:
      copies, matches = matchHistory.pop(0)
      total += copies
      for i in range(matches):
         matchHistory[i] = (matchHistory[i][0] + copies, matchHistory[i][1])
   
   return total

print(part2())