
class Day04:
    def __init__(self, input):
        self.input = []
        for line in input:
            self.input.append(list(line))

    def solve(self):
        part1 = 0
        width = len(self.input[0])
        height = len(self.input)
        for y in range(height):
            for x in range(width):
                if x < width - 3:
                    part1 += self.match(self.input[y][x], self.input[y][x + 1], self.input[y][x + 2], self.input[y][x + 3])
                    if y < height - 3:
                        part1 += self.match(self.input[y][x], self.input[y + 1][x + 1], self.input[y + 2][x + 2], self.input[y + 3][x + 3])
                if y < height - 3:
                    part1 += self.match(self.input[y][x], self.input[y + 1][x], self.input[y + 2][x], self.input[y + 3][x])
                if y < height - 3 and x > 2:
                    part1 += self.match(self.input[y][x], self.input[y + 1][x - 1], self.input[y + 2][x - 2], self.input[y + 3][x - 3])
        print("part1: ", str(part1))

        part2 = 0
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if self.input[y][x] != 'A': continue
                if (self.input[y-1][x-1] == 'M' and self.input[y+1][x+1] == 'S') or (self.input[y-1][x-1] == 'S' and self.input[y+1][x+1] == 'M'):
                    if (self.input[y-1][x+1] == 'M' and self.input[y+1][x-1] == 'S') or (self.input[y-1][x+1] == 'S' and self.input[y+1][x-1] == 'M'):
                        part2 += 1
        print("part2: ", str(part2))


    @staticmethod
    def match(a, b, c, d):
        if a == 'X' and b == 'M' and c == 'A' and d == 'S': return 1
        if a == 'S' and b == 'A' and c == 'M' and d == 'X': return 1
        return 0

with open("Input04.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day04(lines)
day.solve()
