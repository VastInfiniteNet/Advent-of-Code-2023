def part1():
   total = 0
   with open("{}/input".format(__file__[-8:-3])) as f:
      readings = [list(map(int, line.strip().split())) for line in f] 

   for r in readings:
      rows = [r]
      while set(rows[-1]) != set([0]):
         rows.append([rows[-1][i] - rows[-1][i-1] for i in range(1, len(rows[-1]))])
      
      while len(rows) > 1: # predict readings changes
         rows[-2].append(rows[-1][-1] + rows[-2][-1])
         rows.pop()
      total += rows[0][-1]
   
   return "Title: " + str(total)

def part2():
   total = 0
   with open("{}/input".format(__file__[-8:-3])) as f:
      readings = [list(map(int, line.strip().split())) for line in f] 

   for r in readings:
      rows = [r]
      while set(rows[-1]) != set([0]):
         rows.append([rows[-1][i] - rows[-1][i-1] for i in range(1, len(rows[-1]))])
      
      while len(rows) > 1: # predict readings changes
         rows[-2] = [rows[-2][0] - rows[-1][0]] + rows[-2]
         rows.pop()
      total += rows[0][0]

   return "Title: " + str(total)

print(part1())