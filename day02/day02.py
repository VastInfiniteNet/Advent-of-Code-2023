import re

max_cube_count = {
   "red": 12,
   "green": 13,
   "blue": 14
}

def part1():
   def RoundCheck(gameRound):
      for i in range(0, len(gameRound), 2):
         cubeCount, cubeColor = gameRound[i], gameRound[i+1]
         if max_cube_count[cubeColor] < int(cubeCount):
            return False
      return True
   def GameCheck(game):
      for gameRound in game:
         if not RoundCheck(gameRound):
            return False
      return True
   
   total = 0
   i = 0
   with open("day02/day02.txt") as f:
      for line in f:
         gameTitle, *gameRounds = re.split('; |: ', line.strip())
         gameId = int(gameTitle.split()[1])
         gameRounds = [re.split(', | ', game) for game in gameRounds]
         if GameCheck(gameRounds):
            total += gameId
   print("Total:", total)

def part2():
   total = 0
   with open("day02/day02.txt") as f:
      for line in f:
         cubeCounts = {"red": 0, "green": 0, "blue": 0}
         gameRounds = re.split('; |: ', line.strip())[1:]
         gameRounds = [re.split(', | ', game) for game in gameRounds]
         for r in gameRounds:
            while r:
               color, count = r.pop(), int(r.pop())
               if count > cubeCounts[color]:
                  cubeCounts[color] = count
         total += cubeCounts['red'] * cubeCounts['green'] * cubeCounts['blue']
   print(total)
               

if __name__ == "__main__":
   part2()