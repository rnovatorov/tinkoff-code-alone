import sys


def read_sensor_coords():
    n = int(sys.stdin.readline())
    assert n > 0

    sensor_coords = []

    for line in sys.stdin:
        parts = line.split()
        assert len(parts) == 2

        coords = tuple(int(p) for p in parts)
        assert all(v > 0 for v in coords)

        sensor_coords.append(coords)

    assert len(sensor_coords) == n
    return sensor_coords


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x2 - x1) + abs(y2 - y1)


def determine_mean_point(sensor_coords):
    min_x, min_y = float("+inf"), float("+inf")
    max_x, max_y = float("-inf"), float("-inf")

    for (x1, y1) in sensor_coords:
        min_x, min_y = min(min_x, x1), min(min_y, y1)
        max_x, max_y = max(max_x, x1), max(max_y, y1)

    mean_x = (min_x + max_x) // 2
    mean_y = (min_y + max_y) // 2

    return (mean_x, mean_y)


def calc_total_distance(sensor_coords, p1):
    return sum(distance(p1, p2) for p2 in sensor_coords)


def optimize(sensor_coords, p):
    d = calc_total_distance(sensor_coords, p)
    x, y = p

    while True:
        new_x = x - 1
        new_d = calc_total_distance(sensor_coords, (new_x, y))
        if new_d > d:
            break
        x = new_x
        d = new_d

    while True:
        new_y = y - 1
        new_d = calc_total_distance(sensor_coords, (x, new_y))
        if new_d > d:
            break
        y = new_y
        d = new_d

    return (x, y)


def main():
    sensor_coords = read_sensor_coords()
    mean_point = determine_mean_point(sensor_coords)
    print(mean_point, sum(mean_point))
    opt = optimize(sensor_coords, mean_point)
    print(opt, sum(opt))


if __name__ == "__main__":
    main()
