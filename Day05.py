
class Day05:
    def __init__(self, data):
        self.must_be_after = {}
        self.must_be_before = {}
        self.updates = []
        for line in data:
            if '|' in line:
                parts = line.split('|')
                if parts[0] not in self.must_be_before: self.must_be_before[parts[0]] = set()
                self.must_be_before[parts[0]].add(parts[1])
                if parts[1] not in self.must_be_after: self.must_be_after[parts[1]] = set()
                self.must_be_after[parts[1]].add(parts[0])
            if ',' in line:
                self.updates.append(line.split(','))


    def solve(self):
        part1 = 0
        part2 = 0
        for update in self.updates:
            if self.is_legal(update):
                part1 += int(update[int(len(update)/2)])
            else:
                reordered = self.reorder(update)
                part2 += int(reordered[int(len(reordered)/2)])
        print("part1: ", str(part1))
        print("part2: ", str(part2))

    def is_legal(self, update):
        for i in range(len(update) - 1):
            before = update[i]
            rule = self.must_be_after.get(before, set())
            for j in range(i + 1, len(update)):
                after = update[j]
                if after in rule:
                    # before must_be_after after, but it comes before
                    return False
        return True

    def reorder(self, update):
        to_reorder = update.copy()
        reordered = []
        while len(to_reorder) > 0:
            for i in range(len(to_reorder)):
                current = to_reorder[i]
                if self.can_be_first(current, to_reorder):
                    reordered.append(current)
                    to_reorder.pop(i)
                    break
        return reordered

    def can_be_first(self, current, update):
        for after in update:
            rule = self.must_be_before.get(after, set())
            if current in rule:
                # after must_be_before current, so current can't be first
                return False
        return True


with open("Input05.txt") as file:
    lines = [line.rstrip() for line in file]
day = Day05(lines)
day.solve()
