from Point import Point

class Day06:
    def __init__(self, data):
        self.input = []
        for line in data:
            self.input.append(list(line))
        self.width = len(self.input[0])
        self.height = len(self.input)
        self.start_pos = Point(0, 0)
        self.start_dir = 'v'
        for y in range(self.height):
            for x in range(self.width):
                match self.input[y][x]:
                    case '^' | '>' | '<' | 'v':
                        self.start_pos = Point(x, y)
                        self.start_dir = self.input[y][x]

    def solve(self):
        part1 = 0
        guard_pos = self.start_pos
        guard_dir = self.start_dir

        while 0 <= guard_pos.x < self.width and 0 <= guard_pos.y < self.height:
            if self.input[guard_pos.y][guard_pos.x] != 'X':
                part1 += 1
                self.input[guard_pos.y][guard_pos.x] = 'X'
            guard_dir, guard_pos = self.move_guard(guard_dir, guard_pos)

        print("part1: ", str(part1))

        part2 = 0

        for y in range(self.height):
            for x in range(self.width):
                if self.input[y][x] == 'X':
                    self.input[y][x] = '#'
                    if self.is_loop():
                        part2 += 1
                    self.input[y][x] = 'X'
        print("part2: ", str(part2))

    def is_loop(self):
        guard_pos = self.start_pos
        guard_dir = self.start_dir
        visited = set()
        while 0 <= guard_pos.x < self.width and 0 <= guard_pos.y < self.height:
            position = str(guard_pos.x) + guard_dir + str(guard_pos.y)
            if position in visited: return True
            visited.add(position)
            guard_dir, guard_pos = self.move_guard(guard_dir, guard_pos)
        return False

    def move_guard(self, guard_dir, guard_pos):
        new_pos = Point(0, 0)
        match guard_dir:
            case '^':
                new_pos = Point(guard_pos.x, guard_pos.y - 1)
            case '>':
                new_pos = Point(guard_pos.x + 1, guard_pos.y)
            case '<':
                new_pos = Point(guard_pos.x - 1, guard_pos.y)
            case 'v':
                new_pos = Point(guard_pos.x, guard_pos.y + 1)
        if 0 <= new_pos.x < self.width and 0 <= new_pos.y < self.height and self.input[new_pos.y][new_pos.x] == '#':
            match guard_dir:
                case '^':
                    guard_dir = '>'
                case '>':
                    guard_dir = 'v'
                case '<':
                    guard_dir = '^'
                case 'v':
                    guard_dir = '<'
        else:
            guard_pos = new_pos
        return guard_dir, guard_pos


with open("Input06.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day06(lines)
day.solve()
