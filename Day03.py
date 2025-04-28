import re

class Day03:
    def __init__(self, input):
        self.input = input
        self.mul_regexp = re.compile(r"mul\((\d+),(\d+)\)")
        self.dont_do_regexp = re.compile(r"don't\(\).*?do\(\)")

    def solve(self):
        line = ''.join(self.input)
        print("Part 1: " + str(self.multiply(line)))

        clean = re.sub(self.dont_do_regexp, "", line)
        if "don't()" in clean:
            clean = clean[:clean.index("don't()")]
        print("Part 2: " + str(self.multiply(clean)))

    def multiply(self, line):
        result = 0
        parts = self.mul_regexp.findall(line)
        for (a, b) in parts:
            result += int(a) * int(b)
        return result

with open("Input03.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day03(lines)
day.solve()
