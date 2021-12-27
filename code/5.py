import sys


def main():
    num_digits, index = [int(v) for v in sys.stdin.readline().split()]

    code = []
    for line in sys.stdin:
        options = [int(o) for o in line.split()]
        code.append(options)

    def generate_options(i=0):
        if i == len(code):
            yield ()
            return

        for o in code[i]:
            for v in generate_options(i + 1):
                yield (o,) + v

    h = []

    for o in generate_options():
        h.append(o)

    h.sort()

    print("".join(str(v) for v in h[index - 1]))


if __name__ == "__main__":
    main()
