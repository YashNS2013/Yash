import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def get_closeset_pair(arr):
    i = 0
    min_d = math.inf
    min_p1 = None
    min_p2 = None

    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            d = get_distance(arr[i], arr[j])
            if d < min_d:
                min_d = d
                min_p1 = arr[i]
                min_p2 = arr[j]
            j += 1
        i += 1

    return min_d, min_p1, min_p2


# Example test
pts = [Point(0,0), Point(3,4), Point(1,1)]
print(get_closeset_pair(pts))
