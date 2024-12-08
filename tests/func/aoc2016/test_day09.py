import pytest
from aoc2016.day09 import Run_2016_09, decompression_length, decompression_length2


class Test_2016_09:
    def setup_class(self):
        self.day = Run_2016_09()

    def test_bringup_a(self):
        assert decompression_length("ADVENT") == 6
        assert decompression_length("A(1x5)BC") == 7
        assert decompression_length("(3x3)XYZ") == 9
        assert decompression_length("A(2x2)BCD(2x2)EFG") == 11
        assert decompression_length("(6x1)(1x3)A") == 6
        assert decompression_length("X(8x2)(3x3)ABCY") == 18

    def test_bringup_b(self):
        assert decompression_length2("(3x3)XYZ") == 6
        assert decompression_length2("X(8x2)(3x3)ABCY") == 6
        assert decompression_length2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 6
        assert (
            decompression_length2(
                "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
            )
            == 6
        )

    def test_regression_a(self):
        assert self.day.run_part("a") == 150914

    @pytest.mark.xfail
    def test_regression_b(self):
        assert self.day.run_part("b") == 0
