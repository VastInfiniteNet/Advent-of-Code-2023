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
            
   print("Measuring distances")
   distanceGraph = {startPos: 0}
   queue, explored = [startPos], set()
   while queue: # BFS distance labelling
      current = queue.pop(0)
      explored.add(current)
      nexts = graph[current]
      for node in nexts:
         if node not in explored:
            distanceGraph[node] = distanceGraph[current] + 1
            if distanceGraph[node] > furthestDistance:
               furthestDistance, furthestPos = distanceGraph[node], node
            queue.append(node)
   print("Distances:", distanceGraph)
   

   return "Furthest: " + str(furthestDistance) + ", Node: " + str(furthestPos)

def part2():
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

print(part2())