#!/usr/bin/env python3
"""A small, turn-based terminal Snake game."""

import random


WIDTH = 12
HEIGHT = 8
DIRECTIONS = {
    "w": (0, -1),
    "a": (-1, 0),
    "s": (0, 1),
    "d": (1, 0),
}


def place_food(snake):
    """Choose an empty square for the next piece of food."""
    empty_squares = [
        (x, y)
        for y in range(HEIGHT)
        for x in range(WIDTH)
        if (x, y) not in snake
    ]
    return random.choice(empty_squares) if empty_squares else None


def draw_board(snake, food, score):
    """Print the current game board."""
    print("\n" + "+" + "-" * WIDTH + "+")
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            position = (x, y)
            if position == snake[0]:
                row.append("O")
            elif position in snake:
                row.append("o")
            elif position == food:
                row.append("*")
            else:
                row.append(" ")
        print("|" + "".join(row) + "|")
    print("+" + "-" * WIDTH + "+")
    print(f"Score: {score}")


def main():
    snake = [(5, 4), (4, 4), (3, 4)]
    food = place_food(snake)
    score = 0

    print("Mini Snake")
    print("Move with W, A, S, D. Enter Q to quit.")

    while True:
        draw_board(snake, food, score)

        try:
            move = input("Your move: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing!")
            return

        if move == "q":
            print("Thanks for playing!")
            return
        if move not in DIRECTIONS:
            print("Please enter W, A, S, D, or Q.")
            continue

        dx, dy = DIRECTIONS[move]
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)
        ate_food = new_head == food
        body_to_check = snake if ate_food else snake[:-1]

        hit_wall = not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)
        if hit_wall or new_head in body_to_check:
            draw_board(snake, food, score)
            print(f"Game over! Final score: {score}")
            return

        snake.insert(0, new_head)
        if ate_food:
            score += 1
            food = place_food(snake)
            if food is None:
                draw_board(snake, food, score)
                print("You filled the board. You win!")
                return
        else:
            snake.pop()


if __name__ == "__main__":
    main()
