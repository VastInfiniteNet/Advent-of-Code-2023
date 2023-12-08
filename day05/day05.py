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



print(part1())
