def part1():
   total = 0
   f = open("{}/input".format(__file__[-8:-3]))
   for line in f:
      print(line)
   
   f.close()
   
   return "Title: " + str(total)

def part2():
   total = 0
   f = open("{}/input".format(__file__[-8:-3]))
   f.close()
   
   return "Title: " + str(total)

print(part1())