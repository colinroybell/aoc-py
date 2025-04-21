import pytest
from codyssi2025.day08 import Run_2025_08, reduce


class Test_2025_08:
    def setup_class(self):
        self.day = Run_2025_08()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 52

    def test_bringup_2_1(self):
        assert reduce("baa3") == "ba"

    def test_bringup_2_2(self):
        assert reduce("321ab") == "3"

    def test_bringup_2_3(self):
        assert reduce("a7b") == "a" or reduce("a7b") == "b"

    def test_bringup_2_4(self):
        assert reduce("z-4") == "z"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 18

    def test_bringup_3_1(self):
        assert reduce("baa3", part=3) == "ba"

    def test_bringup_3_2(self):
        assert reduce("321ab", part=3) == "3"

    def test_bringup_3_3(self):
        assert reduce("a7b", part=3) == "a" or reduce("a7b", part=3) == "b"

    def test_bringup_3_4(self):
        assert reduce("z-4", part=3) == "z-4"

    def test_bringup_3_5(self):
        assert reduce("a3-b6", part=3) == "-"

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 26

    def test_regression_1(self):
        assert self.day.run_part("1") == 4685

    def test_regression_2(self):
        assert self.day.run_part("2") == 800

    def test_regression_3(self):
        assert self.day.run_part("3") == 1400
