def part1():
   f = open("day05/day05.txt")
   seeds = list(map(int, f.readline()[6:].split()))
   line = f.readline()
   mapPoints = []
   def mapSeed(seed): # check where current seed value should be mapped to
      for point in mapPoints:
         if seed >= point[0] and seed <= point[1]:
            return seed + point[2]
      return seed
   
   while line:
      f.readline()
      line = f.readline()
      mapPoints = []
      while line and line != "\n":
         mapOut, mapIn, mapWidth = list(map(int, line.strip().split()))
         mapPoints.append((mapIn, mapIn + mapWidth - 1, mapOut - mapIn))
         line = f.readline()
      mapPoints.sort(key=lambda x: x[0])
      print(mapPoints)
      seeds = [mapSeed(seed) for seed in seeds]
   
   f.close()
   return min(seeds)


def mapPair(pair, mapPoints): # check where current seed value should be mapped to
      start, end = pair
      best = (100 ** 10, 100 ** 10)
      for i in range(len(mapPoints) - 1):
         left, right = mapPoints[i], mapPoints[i + 1]
         if end < left[0] or start > right[0]:
            continue
         value = min(right[0], end) + right[1]
         if value < best[1]:
            best = (min(right[0], end), value)
      return best
   
def mergeMaps(old, new):
   updatedPoints = []
   print("OLD:", old, "\nNEW:", new, '\n')
   while old and new:
      if new[0][0] < old[0][0]: # new first
         point = new.pop(0)
         other = old
         if len(other) % 2 == 1: # point within band
            point[1] += other[0][1]
      elif new[0][0] > old[0][0]: # old first
         point = old.pop(0)
         other = new
         if len(other) % 2 == 1: # point within band
            point[1] += other[0][1]
      else: # both
         point = old.pop(0)
         point[1] = new.pop(0)[1]
      updatedPoints.append(point)
   if old:
      updatedPoints += old
   else:
      updatedPoints += new
   
   return updatedPoints

def part2():
   f = open("day05/day05.txt")
   seeds = list(map(int, f.readline()[6:].split())) # TODO: RANGIFY
   seedPairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
   line = f.readline()
   maps = []
   mapPoints = []
   
   while line:
      f.readline()
      line = f.readline()
      newMapPoints = []
      while line and line != "\n":
         mapOut, mapIn, mapWidth = list(map(int, line.strip().split()))
         newMapPoints.append([mapIn, mapIn + mapWidth - 1, mapOut - mapIn])
         line = f.readline()
      newMapPoints.sort(key=lambda x: x[0])
      print(newMapPoints)
   
   
   f.close()

print(part2())
