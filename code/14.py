import collections
import sys
import string


def main():
    n, k = [int(v) for v in sys.stdin.readline().split()]
    assert n > 0
    assert k > 0

    raw_restrictions = [line.split() for line in sys.stdin]
    assert len(raw_restrictions) == k

    restrictions = collections.defaultdict(set)

    for parts in raw_restrictions:
        pos, c = int(parts[0]) - 1, parts[1]
        assert pos < n
        assert "A" <= c <= "Z"

        restrictions[pos].add(c)

    print(determine_password(n, restrictions))


def determine_password(n, restrictions):
    password = []

    for i in range(n):
        options = [c for c in string.ascii_uppercase if c not in restrictions[i]]
        c = median(options)

        print(i, options, c)

        password.append(c)

    return "".join(password)


def median(abc):
    if len(abc) % 2 == 0:
        return abc[(len(abc) // 2) - 1]

    return abc[len(abc) // 2]


if __name__ == "__main__":
    main()
