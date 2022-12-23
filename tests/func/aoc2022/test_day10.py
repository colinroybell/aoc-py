import pytest
from aoc2022.day10 import Run_2022_10


class Test_2022_10:
    def setup_class(self):
        self.day = Run_2022_10()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 13140

    def test_bringup_b(self):
        assert (
            self.day.run_part("b", "test1")
            == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
        )

    def test_regression_a(self):
        assert self.day.run_part("a") == 13740

    def test_regression_b(self):
        assert (
            self.day.run_part("b")
            == """####.#..#.###..###..####.####..##..#....
...#.#..#.#..#.#..#.#....#....#..#.#....
..#..#..#.#..#.#..#.###..###..#....#....
.#...#..#.###..###..#....#....#....#....
#....#..#.#....#.#..#....#....#..#.#....
####..##..#....#..#.#....####..##..####.
"""
        )
