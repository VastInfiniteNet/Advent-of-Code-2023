def part1():
   furthestDistance, furthestPos = 0, (0,0)
   # [[TOP,BOTTOM],[LEFT,RIGHT])
   IGNORE, START = '.', 'S'
   translate = { '|': ((True,True),(False,False)), '-': ((False,False),(True,True)), 
                'L': ((True,False),(False,True)), 'J': ((True,False),(True,False)), 
                '7': ((False,True),(True,False)), 'F': ((False,True),(False,True)),
                'S': ((True, True), (True, True))}
   
   symbolPos, graph = {}, {}
   startPos = ()
   lineNum = 0 
   with open("{}/input".format(__file__[-8:-3])) as f: # save non empty symbols
      for line in f:
         for x in range(len(line.strip())):
            if line[x] == IGNORE:
               continue
            if line[x] == START:
               startPos = (x, lineNum)
                  
            symbolPos[(x, lineNum)] = line[x]
         lineNum += 1
         
   def goFromTo(a, b, direction): # can go from a to b
      return a[direction] and b[1-direction]
         
   def successors(currentPos, currentPipe): # get pipes that are connected to a pipe 
      travel = translate[currentPipe]
      nextPipes, candidates = [], []
      candidates.append([(currentPos[0], currentPos[1]-1), [0,0]]) # up
      candidates.append([(currentPos[0], currentPos[1]+1), [0,1]]) # down
      candidates.append([(currentPos[0]-1, currentPos[1]), [1,0]]) # left
      candidates.append([(currentPos[0]+1, currentPos[1]), [1,1]]) # right
      for cand, direction in candidates:
         if cand in symbolPos and travel[direction[0]][direction[1]] and \
               goFromTo(travel[direction[0]], translate[symbolPos[cand]][direction[0]], direction[1]):
            nextPipes.append(cand)
      return nextPipes
   
   print("Starting at:", startPos)
   
   print("Mapping out valid pipes")
   queue = [startPos]
   while queue: # map out valid pipes
      current = queue.pop(0)
      nexts = successors(current, symbolPos[current])
      graph[current] = nexts
      for node in nexts:
         if node not in graph:
            queue.append(node)
   print(graph)
            
   # janky - going through entire chain
   queue, explored = [startPos], set([startPos, graph[startPos][0]])
   current = graph[startPos][0] # start one side of the chain
   current = [node for node in graph[current] if node not in explored][0]
   explored.remove(startPos)
   explored.add(current)
   totalDistance = 2 # 2nd step into chain
   while current != startPos: # loook for other side of chain
      current = [node for node in graph[current] if node not in explored][0]
      explored.add(current)
      totalDistance += 1
      
   return int(totalDistance/2)

def part2():
   total = 0
   with open("{}/input".format(__file__[-8:-3])) as f:
      readings = [list(map(int, line.strip().split())) for line in f] 

   return "Title: " + str(total)

print(part1())