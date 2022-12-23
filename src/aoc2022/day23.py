from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.grid_2d import Grid2d
from utils.vec_2d import Vec2d


class Run_2022_23(DayBase):
    YEAR = "2022"
    DAY = "23"


def proposed_move(grid, pos, prop):
    if (
        not grid.get(pos + Vec2d(-1, -1))
        and not grid.get(pos + Vec2d(0, -1))
        and not grid.get(pos + Vec2d(1, -1))
        and not grid.get(pos + Vec2d(-1, 1))
        and not grid.get(pos + Vec2d(0, 1))
        and not grid.get(pos + Vec2d(1, 1))
        and not grid.get(pos + Vec2d(-1, 0))
        and not grid.get(pos + Vec2d(1, 0))
    ):
        return pos
    for c in prop:
        if c == "N":
            if (
                not grid.get(pos + Vec2d(-1, -1))
                and not grid.get(pos + Vec2d(0, -1))
                and not grid.get(pos + Vec2d(1, -1))
            ):
                return pos + Vec2d(0, -1)
        if c == "S":
            if (
                not grid.get(pos + Vec2d(-1, 1))
                and not grid.get(pos + Vec2d(0, 1))
                and not grid.get(pos + Vec2d(1, 1))
            ):
                return pos + Vec2d(0, 1)
        if c == "W":
            if (
                not grid.get(pos + Vec2d(-1, -1))
                and not grid.get(pos + Vec2d(-1, 0))
                and not grid.get(pos + Vec2d(-1, 1))
            ):
                return pos + Vec2d(-1, 0)
        if c == "E":
            if (
                not grid.get(pos + Vec2d(1, -1))
                and not grid.get(pos + Vec2d(1, 0))
                and not grid.get(pos + Vec2d(1, 1))
            ):
                return pos + Vec2d(1, 0)
    return pos


def part_a(input):
    grid = Grid2d()
    grid.read_from_hash_dot_file(input)
    prop = "NSWE"
    for _ in range(10):
        prop_grid = Grid2d()
        new_grid = Grid2d()
        moves = []
        for pos_t, _ in grid.generator():
            pos = Vec2d(pos_t[0], pos_t[1])
            proposed = proposed_move(grid, pos, prop)
            moves.append((pos, proposed))
            existing = prop_grid.get(proposed)
            if existing:
                prop_grid.set(proposed, existing + 1)
            else:
                prop_grid.set(proposed, 1)
        for move in moves:
            if prop_grid.get(move[1]) == 1:
                new_grid.set(move[1], 1)
            else:
                new_grid.set(move[0], 1)
        (x_start, y_start, width, height) = new_grid.get_dimensions()
        grid = new_grid
        prop = prop[1:] + prop[0]
    (x_start, y_start, width, height) = grid.get_dimensions()
    return (width - x_start) * (height - y_start) - grid.count_non_zero()


def part_b(input):
    grid = Grid2d()
    grid.read_from_hash_dot_file(input)
    prop = "NSWE"
    round = 0
    move_made = True
    while move_made:
        round += 1
        move_made = False
        prop_grid = Grid2d()
        new_grid = Grid2d()
        moves = []
        for pos_t, _ in grid.generator():
            pos = Vec2d(pos_t[0], pos_t[1])
            proposed = proposed_move(grid, pos, prop)
            moves.append((pos, proposed))
            existing = prop_grid.get(proposed)
            if existing:
                prop_grid.set(proposed, existing + 1)
            else:
                prop_grid.set(proposed, 1)
        for move in moves:
            if prop_grid.get(move[1]) == 1:
                new_grid.set(move[1], 1)
                if move[0] != move[1]:
                    move_made = True
            else:
                new_grid.set(move[0], 1)
        (x_start, y_start, width, height) = new_grid.get_dimensions()
        grid = new_grid
        prop = prop[1:] + prop[0]
    return round


if __name__ == "__main__":
    Run_2022_23().run_cmdline()
