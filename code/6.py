import sys


MOVE_UP = "U"
MOVE_DOWN = "D"
MOVE_LEFT = "L"
MOVE_RIGHT = "R"


def main():
    moves = sys.stdin.readline().strip()

    x, y = 0, 0

    for move in moves:
        if move == MOVE_UP:
            y += 1
        elif move == MOVE_DOWN:
            y -= 1
        elif move == MOVE_LEFT:
            x -= 1
        elif move == MOVE_RIGHT:
            x += 1
        else:
            raise ValueError("invalid move", move)

    print(x, y)


if __name__ == "__main__":
    main()
