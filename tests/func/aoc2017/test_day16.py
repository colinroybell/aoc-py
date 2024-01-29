import pytest
from aoc2017.day16 import Run_2017_16


class Test_2017_16:
    def setup_class(self):
        self.day = Run_2017_16()

    def test_bringup_a(self):
        assert self.day.run_part("a", "test1", length=5) == "baedc"

    def test_regression_a(self):
        assert self.day.run_part("a") == "nlciboghjmfdapek"

    def test_regression_b(self):
        assert self.day.run_part("b") == "nlciboghmkedpfja"
