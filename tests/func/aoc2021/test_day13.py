import pytest
from aoc2021.day13 import Run_2021_13


class Test_2021_13:
    def setup_class(self):
        self.day = Run_2021_13()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 17

    def test_bringup_b(self):
        assert (
            self.day.run_part("b", "test1")
            == "#####\n#...#\n#...#\n#...#\n#####\n.....\n.....\n"
        )

    def test_regression_a(self):
        assert self.day.run_part("a") == 788

    def test_regression_b(self):
        # KJBKEUBG
        assert (
            self.day.run_part("b")
            == "#..#...##.###..#..#.####.#..#.###...##..\n#.#.....#.#..#.#.#..#....#..#.#..#.#..#.\n##......#.###..##...###..#..#.###..#....\n#.#.....#.#..#.#.#..#....#..#.#..#.#.##.\n#.#..#..#.#..#.#.#..#....#..#.#..#.#..#.\n#..#..##..###..#..#.####..##..###...###.\n"
        )
