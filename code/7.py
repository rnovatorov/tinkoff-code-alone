import sys


def main():
    _ = int(sys.stdin.readline())

    zeroes = []

    for i, line in enumerate(sys.stdin):
        parts = line.strip().split()

        num_parts = int(parts[0])
        assert len(parts[1:]) == num_parts

        if num_parts == 0:
            print(i, line)
            zeroes.append(i + 1)

    print(sum(zeroes))


if __name__ == "__main__":
    main()
