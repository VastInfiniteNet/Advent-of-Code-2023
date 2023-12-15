def part1():
   total = 0
   readings = []   
   f = open("{}/input".format(__file__[-8:-3]))
   for line in f:
      readings.append(list(map(int, line.strip().split())))
   f.close()

   for r in readings:
      rows = [r]
      while set(rows[-1]) != set([0] * len(rows[-1])):
         rows.append([rows[-1][i] - rows[-1][i-1] for i in range(1, len(rows[-1]))])
      
      print(rows)
      while len(rows) > 1: # predict readings changes
         rows[-2].append(rows[-1][-1] + rows[-2][-1])
         print(rows[-2])
         rows.pop()
      total += rows[0][-1]
      print(rows[0][-1])
      print("\n\n")
   
      
   
   return "Title: " + str(total)

def part2():
   total = 0
   readings = []   
   f = open("{}/input".format(__file__[-8:-3]))
   for line in f:
      readings.append(list(map(int, line.strip().split())))
   f.close()

   for r in readings:
      rows = [r]
      while set(rows[-1]) != set([0] * len(rows[-1])):
         rows.append([rows[-1][i] - rows[-1][i-1] for i in range(1, len(rows[-1]))])
      
      print(rows)
      while len(rows) > 1: # predict readings changes
         rows[-2] = [rows[-2][0] - rows[-1][0]] + rows[-2]
         print(rows[-2])
         rows.pop()
      total += rows[0][0]
      print("\n\n")

print(part1())