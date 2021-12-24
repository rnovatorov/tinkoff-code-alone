import itertools
import sys


def main():
    n = int(sys.stdin.readline())
    assert n > 0

    sizes = [int(v) for v in sys.stdin.readline().split()]
    assert len(sizes) == n

    longest = max(sizes)
    max_area = longest

    for i in range(n):
        size = i + 1
        print(size, end=": ")

        groups = itertools.groupby(sizes, lambda s: s >= size)
        for key, group in groups:
            items = list(group)

            print(key, len(items), end=" ")

            if not key:
                continue

            area = len(items) * size
            max_area = max(area, max_area)
            print(f"(area={area}) ", end="")

        print()

    print(max_area)


if __name__ == "__main__":
    main()
