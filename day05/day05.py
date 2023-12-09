from typing import Self

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
      seeds = [mapSeed(seed) for seed in seeds]
   
   f.close()
   return min(seeds)
   
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

class Transformation:
   def __init__(self, start, end, diff):
      self.start = start
      self.end = end
      self.diff = diff
   def __repr__(self) -> str:
      return "(" + str(self.start) + " -> " + str(self.end) + ", value: " + str(self.diff) +  ")"

class SeedBand:
   def __init__(self, originStart, width, mods):
      self.originStart = originStart
      self.width = width
      self.mods = mods
      
   def start(self):
      return self.originStart + self.mods
      
   def end(self):
      return (self.originStart + self.width - 1) + self.mods
   
   def applyTransformations(self, trans: list[Transformation]) -> list[Self]:
      bands = []
      for tran in trans:
         if self.isDepleted():
            break
         if self.end() < tran.start or self.start() > tran.end: # no overlap
            continue # no applicable transformation
         
         if self.start() < tran.start: # part before tran
            overlapAmount = tran.start - self.start()
            # make new band starting before tran, ending at tran
            bands.append(SeedBand(self.originStart, overlapAmount, self.mods))
            # shrink current band width
            self.width -= overlapAmount
            # move up current bad start
            self.originStart += overlapAmount
         
         # part during tran
         overlapAmount = min(self.end(), tran.end) - self.start() + 1
         bands.append(SeedBand(self.originStart, overlapAmount, self.mods + tran.diff))
         self.width -= overlapAmount
         self.originStart += overlapAmount
            
            
      if not self.isDepleted(): # part after any transition
         bands.append(self)
      return bands
   
   def isDepleted(self) -> bool:
      return self.start() > self.end()
   
   def minSeed(self) -> tuple[int, int]:
      return (self.start(), self.originStart)

def applyTransformations(seedBands: list[SeedBand], transformations: list[Transformation]) -> list[SeedBand]:
   newBands = []
   for band in seedBands:
      newBands += band.applyTransformations(transformations)
   return newBands

def getMinSeed(seedBands: list[SeedBand]) -> tuple[int, int]:
   bandMins = [band.minSeed() for band in seedBands]
   bandMins.sort(key=lambda x: x[0])
   return bandMins[0]

def part2():
   f = open("day05/day05.txt")
   seeds = list(map(int, f.readline()[6:].split())) # TODO: RANGIFY
   seedBands = [SeedBand(seeds[i], seeds[i + 1], 0) for i in range(0, len(seeds), 2)]
   line = f.readline()
   
   while line:
      mapName = f.readline().split('-')[2].split()[0]
      line = f.readline()
      transformations: list[Transformation] = []
      while line and line != "\n":
         mapOut, mapIn, mapWidth = list(map(int, line.strip().split()))
         transformations.append(Transformation(mapIn, mapIn + mapWidth - 1, mapOut - mapIn))
         line = f.readline()
      transformations.sort(key=lambda x: x.start)
      seedBands = applyTransformations(seedBands, transformations)
   
   f.close()
   return getMinSeed(seedBands)

print(part2())
