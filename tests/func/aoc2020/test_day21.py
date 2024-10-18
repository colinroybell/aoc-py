import pytest
from aoc2020.day21 import Run_2020_21


class Test_2020_21:
    def setup_class(self):
        self.day = Run_2020_21()

    def test_regression_a(self):
        assert self.day.run_part("a") == 2315

    def test_regression_b(self):
        assert (
            self.day.run_part("b")
            == "cfzdnz,htxsjf,ttbrlvd,bbbl,lmds,cbmjz,cmbcm,dvnbh"
        )
