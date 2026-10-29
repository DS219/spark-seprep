"""Conway's Game of Life in the terminal.

Seeds a small grid with a glider and a blinker, prints each generation,
and finishes with a short summary.
"""

WIDTH = 12
HEIGHT = 10
GENERATIONS = 8

GLIDER = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
BLINKER = [(8, 6), (9, 6), (10, 6)]


def neighbors(cell):
    x, y = cell
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                yield ((x + dx) % WIDTH, (y + dy) % HEIGHT)


def step(alive):
    counts = {}
    for cell in alive:
        for n in neighbors(cell):
            counts[n] = counts.get(n, 0) + 1
    return {cell for cell, c in counts.items() if c == 3 or (c == 2 and cell in alive)}


def render(alive):
    rows = []
    for y in range(HEIGHT):
        rows.append("".join("#" if (x, y) in alive else "." for x in range(WIDTH)))
    return "\n".join(rows)


def main():
    alive = set(GLIDER + BLINKER)
    for gen in range(GENERATIONS + 1):
        print(f"Generation {gen} ({len(alive)} alive)")
        print(render(alive))
        print()
        alive = step(alive)
    print(f"Done: ran {GENERATIONS} generations on a {WIDTH}x{HEIGHT} wrapping grid.")


if __name__ == "__main__":
    main()
