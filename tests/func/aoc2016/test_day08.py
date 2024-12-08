import pytest
from aoc2016.day08 import Run_2016_08


class Test_2016_08:
    def setup_class(self):
        self.day = Run_2016_08()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", width=7, height=3) == 6

    def test_regression_a(self):
        assert self.day.run_part("a") == 110

    def test_regression_b(self):
        # ZJHRKCPLYJ
        assert (
            self.day.run_part("b")
            == "####...##.#..#.###..#..#..##..###..#....#...#..##.\n...#....#.#..#.#..#.#.#..#..#.#..#.#....#...#...#.\n..#.....#.####.#..#.##...#....#..#.#.....#.#....#.\n.#......#.#..#.###..#.#..#....###..#......#.....#.\n#....#..#.#..#.#.#..#.#..#..#.#....#......#..#..#.\n####..##..#..#.#..#.#..#..##..#....####...#...##..\n"
        )
