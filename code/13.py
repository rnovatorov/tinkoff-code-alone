import sys


def main():
    n, k = [int(v) for v in sys.stdin.readline().split()]
    assert n > 0

    original = [line.strip() for line in sys.stdin]

    normalized = [normalize_number(v) for v in original]

    # longest = max(original, key=len)
    # for i in range(n):
    #    padding = " " * (len(longest) - len(original[i]))
    #    print(original[i], padding, normalized[i])

    assert len(set(normalized)) == len(normalized)
    orig_by_norm = {normalized[i]: original[i] for i in range(n)}

    x = list(sorted(normalized))[k - 1]
    print(x, orig_by_norm[x])


def normalize_number(number):
    country_codes = ["+7", "8"]

    for code in country_codes:
        if number.startswith(code):
            number = number[len(code) :]
            break
    else:
        raise ValueError("unexpected country code", number)

    digits = "".join(c for c in number if c in "0123456789")

    if len(digits) != 10:
        raise ValueError("unexpected len", len(digits))

    return digits


if __name__ == "__main__":
    main()
