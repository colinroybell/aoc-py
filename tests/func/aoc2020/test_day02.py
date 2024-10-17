from aoc2020.day02 import Run_2020_02


class Test_2020_02:
    def setup_class(self):
        self.day = Run_2020_02()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1") == 2

    def test_bringup_b(self):
        assert self.day.run_part("b", "test1") == 1

    def test_regression_a(self):
        assert self.day.run_part("a") == 424

    def test_regression_b(self):
        assert self.day.run_part("b") == 747
