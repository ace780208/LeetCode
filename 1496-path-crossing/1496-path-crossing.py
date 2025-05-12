class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = set()
        coords.add((0, 0))
        x = 0
        y = 0
        for i in range(len(path)):
            if path[i] == 'N':
                y += 1
            elif path[i] == 'S':
                y -= 1
            elif path[i] == 'E':
                x += 1
            else:
                x -= 1
            print((coords))
            if (x, y) in coords:
                return True
            else:
                coords.add((x, y))

        return False

        