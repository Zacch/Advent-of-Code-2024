
class Day07:
    def __init__(self, data):
        self.input = data

    def solve(self):
        part1 = 0
        part2 = 0
        for line in self.input:
            parts = line.split(':')
            test_value = int(parts[0])
            numbers = parts[1].split()
            if self.can_be_true(test_value, numbers): part1 += test_value
            if self.can_be_true_2(test_value, numbers): part2 += test_value

        print("Part 1: " + str(part1))
        print("Part 2: " + str(part2))

    def can_be_true(self, test_value, numbers):
        if len(numbers) == 1: return test_value == int(numbers[0])
        return (self.can_be_true(test_value, [str(int(numbers[0]) + int(numbers[1])), *numbers[2:]])
                or self.can_be_true(test_value, [str(int(numbers[0]) * int(numbers[1])), *numbers[2:]]))


    def can_be_true_2(self, test_value, numbers):
        if len(numbers) == 1: return test_value == int(numbers[0])
        return (self.can_be_true_2(test_value, [str(int(numbers[0]) + int(numbers[1])), *numbers[2:]])
                or self.can_be_true_2(test_value, [str(int(numbers[0]) * int(numbers[1])), *numbers[2:]])
                or self.can_be_true_2(test_value, [numbers[0] + numbers[1], *numbers[2:]]))

with open("Input07.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day07(lines)
day.solve()
