from math import lcm
def part1():
   stepCount = 0
   f = open("day08/day08.txt")
   start, destination = 'AAA', 'ZZZ'
   
   directions = list(f.readline().strip())
   f.readline()
   graph = {}
   for line in f:
      nodeName, leftNode, rightNode = line[0:3], line[7:10], line[12:15]
      graph[nodeName] = (leftNode, rightNode)
   
   currentNode = start
   while currentNode != destination:
      d = directions.pop(0)
      currentNode = graph[currentNode][0 if d == "L" else 1]
      directions.append(d)
      stepCount += 1
   
   f.close()
   return "Steps to reach goal:" + str(stepCount)

def part2():
   f = open("day08/day08.txt")
   
   directions = list(f.readline().strip())
   f.readline()
   graph = {}
   starts = []
   for line in f:
      nodeName, leftNode, rightNode = line[0:3], line[7:10], line[12:15]
      graph[nodeName] = (leftNode, rightNode)
      if nodeName[-1] == 'A':
         starts.append(nodeName)
   f.close()

   chains = [0] * len(starts)
   for i in range(len(starts)):
      currentNode = starts[i]
      while currentNode[-1] != "Z":
         currentNode = graph[currentNode][0 if directions[chains[i] % len(directions)] == "L" else 1]
         chains[i] += 1
   
   return "First destinations aligned step: " + str(lcm(*chains))

print(part1())
print(part2())