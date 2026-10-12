#!/usr/bin/env python3
"""Terminal Pac-Man using only the Python standard library (curses).

Controls: arrow keys or WASD to move, P to pause, Q to quit.
Run in a container with:  podman run -it <image>
"""
import curses
import random
import sys
import time

MAZE = [
    "###################",
    "#o.......#.......o#",
    "#.##.###.#.###.##.#",
    "#.................#",
    "#.##.#.#####.#.##.#",
    "#....#...#...#....#",
    "####.### # ###.####",
    "   #.#   G   #.#   ",
    "####.# ##-## #.####",
    "    .  #GGG#  .    ",
    "####.# ##### #.####",
    "   #.#       #.#   ",
    "####.# ##### #.####",
    "#........#........#",
    "#.##.###.#.###.##.#",
    "#o.#.....P.....#.o#",
    "##.#.#.#####.#.#.##",
    "#....#...#...#....#",
    "#.######.#.######.#",
    "#.................#",
    "###################",
]

DIRS = {
    curses.KEY_UP: (-1, 0), ord("w"): (-1, 0), ord("W"): (-1, 0),
    curses.KEY_DOWN: (1, 0), ord("s"): (1, 0), ord("S"): (1, 0),
    curses.KEY_LEFT: (0, -1), ord("a"): (0, -1), ord("A"): (0, -1),
    curses.KEY_RIGHT: (0, 1), ord("d"): (0, 1), ord("D"): (0, 1),
}
PAC_CHARS = {(-1, 0): "v", (1, 0): "^", (0, -1): ">", (0, 1): "<", (0, 0): "C"}
TICK = 0.13          # seconds per frame
POWER_TICKS = 50     # frames ghosts stay frightened
START_LIVES = 3


class Game:
    def __init__(self):
        self.h = len(MAZE)
        self.w = len(MAZE[0])
        self.walls = set()
        self.dots = set()
        self.pellets = set()
        self.ghost_starts = []
        self.door = None
        for r, row in enumerate(MAZE):
            for c, ch in enumerate(row):
                if ch == "#":
                    self.walls.add((r, c))
                elif ch == ".":
                    self.dots.add((r, c))
                elif ch == "o":
                    self.pellets.add((r, c))
                elif ch == "P":
                    self.pac_start = (r, c)
                elif ch == "G":
                    self.ghost_starts.append((r, c))
                elif ch == "-":
                    self.door = (r, c)
        self.score = 0
        self.lives = START_LIVES
        self.power = 0
        self.frame = 0
        self.reset_positions()

    def reset_positions(self):
        self.pac = self.pac_start
        self.pac_dir = (0, 0)
        self.want_dir = (0, 0)
        self.ghosts = [{"pos": p, "dir": (0, 0), "home": p, "release": i * 15}
                       for i, p in enumerate(self.ghost_starts)]
        self.power = 0

    def wrap(self, r, c):
        return r % self.h, c % self.w

    def open_for_pac(self, pos):
        return pos not in self.walls and pos != self.door

    def open_for_ghost(self, pos):
        return pos not in self.walls

    def step_pac(self):
        r, c = self.pac
        nxt = self.wrap(r + self.want_dir[0], c + self.want_dir[1])
        if self.open_for_pac(nxt):
            self.pac_dir = self.want_dir
        nxt = self.wrap(r + self.pac_dir[0], c + self.pac_dir[1])
        if self.open_for_pac(nxt):
            self.pac = nxt
        if self.pac in self.dots:
            self.dots.discard(self.pac)
            self.score += 10
        elif self.pac in self.pellets:
            self.pellets.discard(self.pac)
            self.score += 50
            self.power = POWER_TICKS

    def step_ghosts(self):
        for i, g in enumerate(self.ghosts):
            if self.frame < g["release"]:
                continue
            # Frightened ghosts move every other frame
            if self.power and self.frame % 2:
                continue
            r, c = g["pos"]
            options = []
            for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nxt = self.wrap(r + d[0], c + d[1])
                # Once out of the house, ghosts don't go back through the door
                if nxt == self.door and r < self.door[0]:
                    continue
                if self.open_for_ghost(nxt):
                    options.append((d, nxt))
            if not options:
                continue
            back = (-g["dir"][0], -g["dir"][1])
            forward = [o for o in options if o[0] != back] or options

            def dist(p):
                return abs(p[0] - self.pac[0]) + abs(p[1] - self.pac[1])

            if (r, c) in self.ghost_starts or (r, c) == self.door:
                # Leave the ghost house: head for the door, then up
                target = (self.door[0] - 2, self.door[1])
                choice = min(forward, key=lambda o: abs(o[1][0] - target[0]) + abs(o[1][1] - target[1]))
            elif self.power:
                choice = max(forward, key=lambda o: dist(o[1]) + random.random())
            elif random.random() < 0.25 + 0.1 * i:
                choice = random.choice(forward)
            else:
                choice = min(forward, key=lambda o: dist(o[1]))
            g["dir"], g["pos"] = choice

    def check_collisions(self):
        for g in self.ghosts:
            if g["pos"] == self.pac:
                if self.power:
                    self.score += 200
                    g["pos"] = g["home"]
                    g["dir"] = (0, 0)
                    g["release"] = self.frame + 20
                else:
                    return True
        return False


def draw(scr, game, msg=""):
    scr.erase()
    maxy, maxx = scr.getmaxyx()
    need_w = game.w * 2 + 2
    if maxy < game.h + 3 or maxx < need_w:
        scr.addstr(0, 0, "Terminal too small - please enlarge it"[: maxx - 1])
        scr.refresh()
        return
    color = curses.has_colors()
    for r, row in enumerate(MAZE):
        for c in range(game.w):
            pos = (r, c)
            y, x = r + 1, c * 2
            if pos in game.walls:
                scr.addstr(y, x, "██", curses.color_pair(1) if color else curses.A_REVERSE)
            elif pos == game.door:
                scr.addstr(y, x, "--")
            elif pos in game.pellets:
                scr.addstr(y, x, "o ", curses.A_BOLD)
            elif pos in game.dots:
                scr.addstr(y, x, ". ")
    for i, g in enumerate(game.ghosts):
        y, x = g["pos"][0] + 1, g["pos"][1] * 2
        if game.power:
            attr = curses.color_pair(6) | curses.A_BOLD if color else curses.A_DIM
            ch = "w"
        else:
            attr = curses.color_pair(3 + i % 3) | curses.A_BOLD if color else curses.A_BOLD
            ch = "M"
        scr.addstr(y, x, ch, attr)
    py, px = game.pac[0] + 1, game.pac[1] * 2
    mouth = PAC_CHARS[game.pac_dir] if game.frame % 2 else "O"
    scr.addstr(py, px, mouth, (curses.color_pair(2) if color else 0) | curses.A_BOLD)
    status = f" SCORE {game.score:<6} LIVES {'C ' * game.lives}"
    scr.addstr(0, 0, status[: maxx - 1], curses.A_BOLD)
    help_line = msg or "Arrows/WASD move  P pause  Q quit"
    scr.addstr(game.h + 1, 0, help_line[: maxx - 1])
    scr.refresh()


def wait_key(scr, keys=None):
    scr.nodelay(False)
    while True:
        k = scr.getch()
        if keys is None or k in keys:
            scr.nodelay(True)
            return k


def main(scr):
    curses.curs_set(0)
    scr.nodelay(True)
    scr.keypad(True)
    if curses.has_colors():
        curses.start_color()
        try:
            curses.use_default_colors()
            bg = -1
        except curses.error:
            bg = curses.COLOR_BLACK
        curses.init_pair(1, curses.COLOR_BLUE, bg)
        curses.init_pair(2, curses.COLOR_YELLOW, bg)
        curses.init_pair(3, curses.COLOR_RED, bg)
        curses.init_pair(4, curses.COLOR_MAGENTA, bg)
        curses.init_pair(5, curses.COLOR_CYAN, bg)
        curses.init_pair(6, curses.COLOR_WHITE, bg)

    game = Game()
    draw(scr, game, "PAC-MAN!  Press any key to start")
    wait_key(scr)

    while True:
        start = time.time()
        k = scr.getch()
        while k != -1:
            if k in (ord("q"), ord("Q")):
                return game.score, "quit"
            if k in (ord("p"), ord("P")):
                draw(scr, game, "PAUSED - press P to resume")
                wait_key(scr, (ord("p"), ord("P")))
            elif k in DIRS:
                game.want_dir = DIRS[k]
            k = scr.getch()

        game.frame += 1
        game.step_pac()
        dead = game.check_collisions()
        if not dead:
            game.step_ghosts()
            dead = game.check_collisions()
        if game.power:
            game.power -= 1

        if dead:
            game.lives -= 1
            if game.lives == 0:
                draw(scr, game, "GAME OVER - press any key")
                time.sleep(0.5)
                wait_key(scr)
                return game.score, "lost"
            draw(scr, game, "Caught! Press any key to continue")
            time.sleep(0.5)
            wait_key(scr)
            game.reset_positions()
            game.frame = 0
            continue

        if not game.dots and not game.pellets:
            draw(scr, game, "YOU WIN! press any key")
            time.sleep(0.5)
            wait_key(scr)
            return game.score, "won"

        draw(scr, game)
        time.sleep(max(0.0, TICK - (time.time() - start)))


if __name__ == "__main__":
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        print("Pac-Man needs an interactive terminal.")
        print("Run it with:  podman run -it <image-name>")
        sys.exit(1)
    try:
        score, result = curses.wrapper(main)
    except KeyboardInterrupt:
        print("Bye!")
        sys.exit(0)
    print({"won": "You cleared the maze!", "lost": "Game over.", "quit": "Thanks for playing!"}[result])
    print(f"Final score: {score}")
