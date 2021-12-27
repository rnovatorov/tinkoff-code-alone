import sys


def main():
    num_ropes, height = [int(v) for v in sys.stdin.readline().split()]

    ropes = []

    for v in sys.stdin.readline().split():
        r = int(v)
        assert r > 0
        ropes.append(r)

    assert len(ropes) == num_ropes

    ropes.sort(reverse=True)

    knots = 0
    lasso = 0

    for r in ropes:
        lasso += r
        if lasso >= height:
            print(knots)
            exit(0)
        knots += 1

    print("oops")
    exit(1)


if __name__ == "__main__":
    main()
