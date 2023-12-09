import math
def part1():
   total = 1
   f = open("day06/day06.txt")
   times = list(map(int,f.readline().strip().split()[1:]))
   distances = list(map(int,f.readline().strip().split()[1:]))
   races = list(zip(times, distances))
   
   for race in races:
      target_distance = race[1]
      ways_to_beat = 0
      for i in range(race[0]):
         distance = i * (race[0] - i)
         if distance > target_distance:
            ways_to_beat += 1
      total *= ways_to_beat
            
   f.close()
   return total

def part2():
   total = 1
   f = open("day06/day06.txt")
   race_time = int(''.join(f.readline().split()[1:]))
   target_distance =  int(''.join(f.readline().split()[1:]))
   square_root_part = (race_time ** 2 - 4*target_distance) ** 0.5
   lower_time = math.ceil((race_time - square_root_part)/2)
   upper_time = math.floor((race_time + square_root_part)/2)
            
   f.close()
   return upper_time - lower_time + 1



print(part2())