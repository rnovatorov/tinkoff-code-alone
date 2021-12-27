import itertools

import primefac


MAX = 99999999999999
MIN = 10000000000000

PRIME_LIMIT = 99999999


def all_primes_under(x):
    prime_gen = primefac.primegen()

    for v in prime_gen:
        if v >= x:
            return

        yield v


def main():
    primes = reversed(list(all_primes_under(PRIME_LIMIT)))

    def generate_candidates():

        window = []

        for p in primes:
            new_window = []
            new_window_needed = False

            for v in window:
                if v - p <= 100:
                    new_window.append(v)
                else:
                    new_window_needed = True

            if not new_window_needed:
                window.append(p)
                continue

            new_window.append(p)

            for (m, n) in itertools.combinations_with_replacement(window, 2):
                product = m * n
                if MIN <= product <= MAX:
                    yield product

            window = new_window

    largest = 0

    for c in generate_candidates():
        if c > largest:
            largest = c
            print(largest)


if __name__ == "__main__":
    main()
