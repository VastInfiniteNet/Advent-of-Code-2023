import re

def part1():
   regex = re.compile(r"([0-9])")
   total = 0
   with open("day01/day01-1.txt") as f:
      for line in f:
         print(line.strip())
         res = regex.findall(line)
         value = int(res[0] + res[-1])
         print(value)
         total = total + value
   print("Total:", total)
   
numbers = {
   "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'
}

def findNumbers(string):
   front = False
   end = False
   for i in range(len(string)):
      if not front:
         front = findNumber(string, i)
      if not end:
         end = findNumber(string, len(string) - 1 - i)
      if front and end:
         return [front, end]
   
def findNumber(string, start = 0):
   for num in numbers.keys():    # number word
      if string.startswith(num, start):
         return num
   for num in numbers.values():  # number symbol
      if string[start] == num:
         return num
   
def part2():
   total = 0
   with open("day01/day01-1.txt") as f:
      for line in f:
         first, last = [int(numbers.get(num, num)) for num in findNumbers(line.strip())]
         total += first * 10 + last
   print("Total:", total)


if __name__ == "__main__":
   part2()