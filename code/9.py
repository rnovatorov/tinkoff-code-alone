import sys


def main():
    n = int(sys.stdin.readline())
    assert n > 0

    rules = [int(v) for v in sys.stdin.readline().split()]
    assert len(rules) == len(set(rules)) == n

    def generate_chain(root):
        src = root
        while True:
            yield src
            dst = rules[src] - 1
            if dst == root:
                return
            src = dst

    chains = map(generate_chain, range(n))
    max_length = max(len(list(c)) for c in chains)

    print(max_length)


if __name__ == "__main__":
    main()
