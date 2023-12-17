def part(gapSpacing):
   total = 0
   f = open("{}/input".format(__file__[-8:-3]))
   lineNum, galaxyList = 0, []
   emptyCols, emptyRows = [], []
   galaxyColPresent, galaxyRowPresent = {}, False
   EMPTY, GALAXY = '.', '#'
   
   # read first line to init emptyCols
   line = f.readline().strip()
   for x in range(len(line.strip())):
      if line[x] == GALAXY:
         galaxyRowPresent = True
         galaxyColPresent[x] = True
         galaxyList.append((lineNum, x))
      else:
         galaxyColPresent[x] = False
   if not galaxyRowPresent: # check if this row is empty
      emptyRows.append(lineNum)
   lineNum += 1
   
   for line in f:
      galaxyRowPresent = False
      for x in range(len(line.strip())):
         if line[x] == GALAXY:
            galaxyRowPresent = True
            galaxyColPresent[x] = True
            galaxyList.append((lineNum, x))
      if not galaxyRowPresent: # check if this row is empty
         emptyRows.append(lineNum)
      lineNum += 1
   for i in range(len(galaxyColPresent)): # check for empty columns
      if not galaxyColPresent[i]:
         emptyCols.append(i)   
   f.close()            
   emptyCols.sort(), emptyRows.sort() # order to make distance checking quicker
   
   def pairDistance(galA, galB):
      dist = 0
      xMin, xMax = min(galA[0], galB[0]), max(galA[0], galB[0])
      yMin, yMax = min(galA[1], galB[1]), max(galA[1], galB[1])
      
      dist += xMax - xMin # x distance
      dist += yMax - yMin # y distance
      def gapCheck(dimList, dimMin, dimMax):
         gaps = 0
         for i in range(len(dimList)): # x gaps
            if dimList[i] > dimMax:
               break  
            if dimList[i] < dimMin:
               continue
            gaps += (gapSpacing - 1)
         return gaps
            
      dist += gapCheck(emptyCols, yMin, yMax)
      dist += gapCheck(emptyRows, xMin, xMax)
      
      return dist
   
   galaxyCount = len(galaxyList)
   for first in range(galaxyCount - 1): # [first: 1 -> 8]
      for second in range(first+1, galaxyCount): # [second: first + 1 -> 9]
         total += pairDistance(galaxyList[first], galaxyList[second])
   
   
   return total

print("Part 1:", part(2))
print("Part 2:", part(1000000))