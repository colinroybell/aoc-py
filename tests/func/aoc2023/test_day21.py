import pytest
from aoc2023.day21 import Run_2023_21


class Test_2023_21:
    def setup_class(self):
        self.day = Run_2023_21()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", steps=5) == 16

    @pytest.mark.parametrize(
        "steps, expected_output",
        [
            (6, 16),
            (10, 50),
            (50, 1594),
            (100, 6536),
            (500, 167004),
            (1000, 668637),
            (5000, 16733044),
        ],
    )
    @pytest.mark.xfail
    def test_bringup_b(self, steps, expected_output):
        assert self.day.run_part("b", "test1", steps=steps) == expected_output

    def test_regression_a(self):
        assert self.day.run_part("a") == 3814

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
