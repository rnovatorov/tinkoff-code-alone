import sys


def main():
    seq = list(sys.stdin.readline().strip())
    assert all(q in "()[]{}" for q in seq)

    state = []
    func_num = 0

    for i, q in enumerate(seq):
        depth = len(state)
        if depth == 0 and q == "{":
            func_num += 1

        if starts_block(q):
            state.append(q)
            continue

        assert ends_block(q), (i, q)

        prev = state.pop()

        if not closes_block(prev, q):
            raise ValueError(i, prev, q)

    print(func_num)


def closes_block(a, z):
    return (a + z == "()") or (a + z == "[]") or (a + z == "{}")


def starts_block(q):
    return q in "([{"


def ends_block(q):
    return q in ")]}"


if __name__ == "__main__":
    main()
