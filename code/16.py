# solution taken from here: https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1

import sys

from PIL import Image, ImageDraw

DRAW = False

images = []

# a = [
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
#    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]


def load_a():
    map_ = []

    a = None
    b = None
    size = None

    for y, line in enumerate(sys.stdin):
        parts = line.split()
        if size is None:
            size = len(parts)

        row = []

        for x, p in enumerate(parts):
            if p == "A":
                assert a is None
                a = (y, x)
                row.append(0)
            elif p == "B":
                assert b is None
                b = (y, x)
                row.append(0)
            elif p == ".":
                row.append(0)
            elif p == "#":
                row.append(1)
            else:
                raise ValueError("unexpected part", p)

        assert len(row) == size

        map_.append(row)

    return map_, a, b


a, start, end = load_a()

zoom = 20
borders = 6


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i - 1][j] == 0 and a[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and a[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and a[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and a[i][j + 1] == 0:
                    m[i][j + 1] = k + 1


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(str(m[i][j]).ljust(2), end=" ")
        print()


def draw_matrix(a, m, the_path=[]):
    if not DRAW:
        return
    im = Image.new("RGB", (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == start[0] and j == start[1]:
                color = (0, 255, 0)
                r = borders
            if i == end[0] and j == end[1]:
                color = (0, 255, 0)
                r = borders
            draw.rectangle(
                (
                    j * zoom + r,
                    i * zoom + r,
                    j * zoom + zoom - r - 1,
                    i * zoom + zoom - r - 1,
                ),
                fill=color,
            )
            if m[i][j] > 0:
                r = borders
                draw.ellipse(
                    (
                        j * zoom + r,
                        i * zoom + r,
                        j * zoom + zoom - r - 1,
                        i * zoom + zoom - r - 1,
                    ),
                    fill=(255, 0, 0),
                )
    for u in range(len(the_path) - 1):
        y = the_path[u][0] * zoom + int(zoom / 2)
        x = the_path[u][1] * zoom + int(zoom / 2)
        y1 = the_path[u + 1][0] * zoom + int(zoom / 2)
        x1 = the_path[u + 1][1] * zoom + int(zoom / 2)
        draw.line((x, y, x1, y1), fill=(255, 0, 0), width=5)
    draw.rectangle(
        (0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0, 255, 0), width=2
    )
    images.append(im)


m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i, j = start
m[i][j] = 1

k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
    draw_matrix(a, m)


i, j = end
k = m[i][j]
the_path = [(i, j)]
while k > 1:
    if i > 0 and m[i - 1][j] == k - 1:
        i, j = i - 1, j
        the_path.append((i, j))
        k -= 1
    elif j > 0 and m[i][j - 1] == k - 1:
        i, j = i, j - 1
        the_path.append((i, j))
        k -= 1
    elif i < len(m) - 1 and m[i + 1][j] == k - 1:
        i, j = i + 1, j
        the_path.append((i, j))
        k -= 1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
        i, j = i, j + 1
        the_path.append((i, j))
        k -= 1
    draw_matrix(a, m, the_path)

for i in range(10):
    if i % 2 == 0:
        draw_matrix(a, m, the_path)
    else:
        draw_matrix(a, m)

# print_m(m)
print(len(the_path))

if DRAW:
    images[0].save(
        "maze.gif",
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=1,
        loop=0,
    )
