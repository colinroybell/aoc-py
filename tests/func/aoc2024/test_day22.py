import pytest
from aoc2024.day22 import Run_2024_22, next_number, score


class Test_2024_22:
    def setup_class(self):
        self.day = Run_2024_22()

    def test_bringup_a_1(self):
        results = [
            15887950,
            16495136,
            527345,
            704524,
            1553684,
            12683156,
            11100544,
            12249484,
            7753432,
            5908254,
        ]
        n = 123
        for i in range(10):
            n = next_number(n)
            assert n == results[i]

    def test_bringup_a_2(self):
        assert self.day.run_part("a", "test1") == 37327623

    def test_bringup_b(self):
        assert score([1, 2, 3, 2024], [-2, 1, -1, 3]) == 23

    def test_regression_a(self):
        assert self.day.run_part("a") == 15303617151

    def test_regression_b(self):
        assert self.day.run_part("b") == 1727
