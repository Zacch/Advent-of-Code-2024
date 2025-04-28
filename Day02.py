from enum import Enum

class State(Enum):
    UNDECIDED = 0
    ASCENDING = 1
    DESCENDING = 2
    UNSAFE = 3

MIN_DIFF = 1
MAX_DIFF = 3

class Day02:
    def __init__(self, input):
        self.input = input

    def part1(self):
        part1 = 0
        part2 = 0
        for line in self.input:
            ints = [int(item) for item in line.split()]
            index = self.unsafe_index(ints)
            if index == 0:
                part1 += 1
            else:
                v1 = ints.copy()
                v1.pop(index - 1)
                if self.unsafe_index(v1) > 0:
                    v2 = ints.copy()
                    v2.pop(index)
                    if self.unsafe_index(v2) > 0:
                        if index != 2: continue
                        v3 = ints.copy()
                        v3.pop(0)
                        if self.unsafe_index(v3) > 0:
                            continue
            part2 += 1
        print("Part 1: " + str(part1))
        print("Part 2: " + str(part2))

    @staticmethod
    def unsafe_index(ints):
        previous = ints[0]
        state = State.UNDECIDED
        for i in range(1, len(ints)):
            current = ints[i]
            diff = abs(current - previous)
            if diff < MIN_DIFF or diff > MAX_DIFF:
                return i
            match state:
                case State.UNDECIDED:
                    if current > previous:
                        state = State.ASCENDING
                    if current < previous:
                        state = State.DESCENDING
                case State.ASCENDING:
                    if current < previous:
                        return i
                case State.DESCENDING:
                    if current > previous:
                        return i
            previous = current
        return 0

with open("Input02.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day02(lines)
day.part1()
