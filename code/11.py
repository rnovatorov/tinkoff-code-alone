import sys


def main():
    n = int(sys.stdin.readline())
    assert n > 0

    screamers = []

    for line in sys.stdin:
        parts = line.strip().split()
        assert len(parts) > 0

        deps_num = int(parts[0])
        deps = set(int(v) - 1 for v in parts[1:])
        assert len(deps) == deps_num

        screamers.append(deps)

    assert len(screamers) == n

    seq = determine_sequence(screamers)
    assert len(seq) == n

    res = sum((i + 1) * s for i, s in enumerate(seq))
    print(res)


def determine_sequence(screamers):
    sequence = []
    activated = set()

    while True:
        updated = False

        for i, deps in enumerate(screamers):
            already_active = i in activated
            if already_active:
                continue

            deps_satisfied = deps.issubset(activated)
            if deps_satisfied:
                activated.add(i)
                sequence.append(i + 1)
                updated = True
                break

        assert updated

        if len(activated) == len(screamers):
            return sequence


if __name__ == "__main__":
    main()
