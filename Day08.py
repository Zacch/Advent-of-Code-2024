from Point import Point

class Day08:
    def __init__(self, data):
        self.input = []
        for line in data:
            self.input.append(list(line))
        self.width = len(self.input[0])
        self.height = len(self.input)
        self.transmitters = {}
        for y in range(self.height):
            for x in range(self.width):
                frequency = self.input[y][x]
                if frequency == '.': continue
                points = self.transmitters.get(frequency, [])
                points.append(Point(x, y))
                self.transmitters[frequency] = points

    def solve(self):
        antinodes = set()
        for frequency in self.transmitters:
            antinodes = antinodes.union(self.calculate_antinodes(self.transmitters[frequency]))
        print("part1: ", str(len(antinodes)))

        antinodes = set()
        for frequency in self.transmitters:
            antinodes = antinodes.union(self.calculate_antinodes_2(self.transmitters[frequency]))
        print("part2: ", str(len(antinodes)))

    def calculate_antinodes(self, locations):
        antinodes = set()
        for a in range(len(locations) - 1):
            for b in range(a + 1, len(locations)):
                p1 = locations[a]
                p2 = locations[b]
                diff = p2 - p1
                self.add_if_in_range(p1 - diff, antinodes)
                self.add_if_in_range(p2 + diff, antinodes)
        return antinodes

    def calculate_antinodes_2(self, locations):
        antinodes = set()
        for a in range(len(locations) - 1):
            for b in range(a + 1, len(locations)):
                p1 = locations[a]
                p2 = locations[b]
                diff = p2 - p1
                p = p1
                while self.in_bounds(p):
                    antinodes.add(str(p))
                    p = p - diff
                p = p2
                while self.in_bounds(p):
                    antinodes.add(str(p))
                    p = p + diff
        return antinodes

    def add_if_in_range(self, p, antinodes):
        if self.in_bounds(p):
            antinodes.add(str(p))

    def in_bounds(self, p):
        return 0 <= p.x < self.width and 0 <= p.y < self.height


with open("Input08.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day08(lines)
day.solve()
