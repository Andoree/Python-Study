class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def on_segment(p, q, r):
    if (max(p.x, r.x) >= q.x >= min(p.x, r.x) and
            max(p.y, r.y) >= q.y >= min(p.y, r.y)):
        return True
    return False


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if (val > 0) else 2


def segment_intersection(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False


def polygon_intersection(points1, points2):
    p1 = points1[0]

    length2 = len(points2)

    orient = orientation(points2[0], p1, points2[1])
    ori_changed = False
    for i in range(1, length2):
        if orient != orientation(p1, points2[i % length2], points2[(i + 1) % length2]):
            ori_changed = True
            break
    if not ori_changed:
        return True

    length1 = len(points1)

    for i in range(0, length1):
        for j in range(0, length2):
            if segment_intersection(points1[i], points1[(i + 1) % length1],
                                    points2[j], points2[(j + 1) % length2]):
                return True
    return False


def circlesIntersection(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    length = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
    if length <= r1 + r2:
        return True
    return False


def main():
    print(polygon_intersection((Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)),
                               (Point(20, 20), Point(20, 30), Point(30, 30), Point(30, 20))))
    print(polygon_intersection((Point(5, 5), Point(5, 15), Point(15, 15), Point(15, 5)),
                               (Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0))))
    print(polygon_intersection((Point(5, 5), Point(5, 15), Point(15, 15), Point(15, 5)),
                               (Point(15, 15), Point(20, 30), Point(30, 30), Point(30, 66))))
    print(polygon_intersection((Point(16, 15), Point(52, 135), Point(125, 125), Point(125, 55)),
                               (Point(0, 0), Point(0, 15), Point(15, 15), Point(15, 0))))
    print(polygon_intersection((Point(15, 15), Point(52, 135), Point(125, 125), Point(125, 55)),
                               (Point(0, 0), Point(0, 15), Point(15, 15), Point(15, 0))))
    print(circlesIntersection((1, 1, 5), (10, 10, 100)))
    print(circlesIntersection((0, 0, 1), (2, 0, 1)))


if __name__ == '__main__': main()
