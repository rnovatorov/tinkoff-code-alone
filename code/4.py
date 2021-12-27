import collections
import sys


def main():
    num_blades = int(sys.stdin.readline())

    blades = collections.deque()

    for v in sys.stdin.readline().split():
        b = int(v)
        assert b > 0
        blades.append(b)

    assert len(blades) == num_blades

    uniq = set()

    for _ in range(num_blades):
        blades.appendleft(blades.pop())
        uniq.add(tuple(v for v in blades))

    print(len(uniq))


if __name__ == "__main__":
    main()
