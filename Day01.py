
class Day01:
    def __init__(self, input):
        self.input = input

    def part1(self):
        part1 = 0
        part2 = 0
        left = []
        right = []
        rights = {}
        for line in self.input:
            parts = line.split()
            left.append(int(parts[0]))
            second = int(parts[1])
            right.append(second)
            if second in rights.keys():
                rights[second] += 1
            else:
                rights[second] = 1

        left.sort()
        right.sort()

        for i in range(len(left)):
            first = left[i]
            part1 += abs(first - right[i])
            part2 += first * rights.get(first, 0)
        print("Part 1: " + str(part1))
        print("Part 2: " + str(part2))


with open("Input01.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day01(lines)
day.part1()
