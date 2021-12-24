import sys
import itertools

KEYBOARD = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}


def main():
    seq = [int(v) for v in sys.stdin.readline().strip()]
    assert len(seq) > 0

    groups = itertools.groupby(reversed(seq))

    result = []

    for digit, group in groups:
        assert digit in KEYBOARD

        group_size = len(list(group))

        letters = KEYBOARD[digit]
        quot, rem = group_size // len(letters), group_size % len(letters)

        chunk = ""

        if rem != 0:
            chunk += letters[rem - 1]

        chunk += quot * letters[-1]

        result.append(chunk)

    print("".join(reversed(result)))


if __name__ == "__main__":
    main()
