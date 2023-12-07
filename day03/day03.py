def part1():
   f = open("day03/day03.txt", 'r')
   
   total, blank = 0, '.'
   prevLine, currentLine, nextLine  = '', f.readline().strip(), f.readline().strip()
   while currentLine:
      currentPart, isPartNumber = '', False
      for i in range(len(currentLine)):
         if currentLine[i].isdigit():
            currentPart += currentLine[i]
            if not isPartNumber:
               if i > 0 and not currentLine[i - 1].isdigit() and currentLine[i - 1] != blank:
                  isPartNumber = True
               elif i > 0 and prevLine and not prevLine[i - 1].isdigit() and prevLine[i - 1] != blank:
                  isPartNumber = True
               elif i > 0 and nextLine and not nextLine[i - 1].isdigit() and nextLine[i - 1] != blank:
                  isPartNumber = True
               elif prevLine and not prevLine[i].isdigit() and prevLine[i] != blank:
                  isPartNumber = True
               elif nextLine and not nextLine[i].isdigit() and nextLine[i] != blank:
                  isPartNumber = True
               elif i < len(currentLine) - 1 and prevLine and not prevLine[i + 1].isdigit() and prevLine[i + 1] != blank:
                  isPartNumber = True
               elif i < len(currentLine) - 1 and not currentLine[i + 1].isdigit() and currentLine[i + 1] != blank:
                  isPartNumber = True
               elif i < len(currentLine) - 1 and nextLine and not nextLine[i + 1].isdigit() and nextLine[i + 1] != blank:
                  isPartNumber = True
         else:
            if currentPart and isPartNumber:
               total += int(currentPart)
               isPartNumber = False
            currentPart = ''
      if currentPart and isPartNumber:
               total += int(currentPart)
               isPartNumber = False
      prevLine, currentLine, nextLine = currentLine, nextLine, f.readline().strip()
         
   f.close()
   return total

def part2():
   f = open("day03/day03.txt", 'r')
   total, lineNum, gearRatios = 0, 0, {}
   prevLine, currentLine, nextLine = '', f.readline().strip(), f.readline().strip()
   gear, gearLocations = '*', set()
   while currentLine:
      currentPart = ''
      gearLocations.clear()
      for i in range(len(currentLine)):
         if currentLine[i].isdigit():
            currentPart += currentLine[i]
            if i > 0 and currentLine[i - 1] == gear:
               gearLocations.add((lineNum, i - 1))
            elif i > 0 and prevLine and prevLine[i - 1] == gear:
               gearLocations.add((lineNum - 1, i - 1))
            elif i > 0 and nextLine and nextLine[i - 1] == gear:
               gearLocations.add((lineNum + 1, i - 1))
            elif prevLine and prevLine[i] == gear:
               gearLocations.add((lineNum - 1, i))
            elif nextLine and nextLine[i] == gear:
               gearLocations.add((lineNum + 1, i))
            elif i < len(currentLine) - 1 and prevLine and prevLine[i + 1] == gear:
               gearLocations.add((lineNum - 1, i + 1))
            elif i < len(currentLine) - 1 and currentLine[i + 1] == gear:
               gearLocations.add((lineNum, i + 1))
            elif i < len(currentLine) - 1 and nextLine and nextLine[i + 1] == gear:
               gearLocations.add((lineNum + 1, i + 1))
         else:
            if currentPart and gearLocations != []:
               for g in gearLocations:
                  gearRatios[g] = gearRatios.get(g, []) + [currentPart]
            gearLocations.clear()
            currentPart = ''
      if currentPart and gearLocations != []:
               for g in gearLocations:
                  gearRatios[g] = gearRatios.get(g, []) + [currentPart]
               gearLocations.clear()
      lineNum += 1
      prevLine, currentLine, nextLine = currentLine, nextLine, f.readline().strip()
   for gearNumbers in gearRatios.values():
      if len(gearNumbers) == 2:
         total += int(gearNumbers[0]) * int(gearNumbers[1])

   f.close()
   return total

if __name__ == "__main__":
   print(part1())