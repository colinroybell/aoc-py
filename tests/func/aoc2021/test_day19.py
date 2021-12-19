import pytest
from aoc2021.day19 import Run_2021_19, Scanner
from utils.vec_3d import Vec3d


class Test_2021_19:
    def setup_class(self):
        self.day = Run_2021_19()

    def test_bringup_a_1(self):
        scanners = Scanner.parse(self.day.input_filename("a", "test1"))
        (match, orientation, position) = scanners[0].match(scanners[1])
        assert match and orientation == 12 and position == Vec3d(-68, 1246, 43)

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test2") == 79

    def test_bringup_b(self):
        assert self.day.run_part("b", "test2") == 3621

    def test_regression_a(self):
        assert self.day.run_part("a") == 385

    def test_regression_b(self):
        assert self.day.run_part("b") == 10707
