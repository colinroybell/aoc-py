import pytest
from ecst02.day02 import Run_st02_02


class Test_st02_02:
    def setup_class(self):
        self.day = Run_st02_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 7

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test2", repeats=5) == 14

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test3", repeats=10) == 304

    def test_bringup_2_3(self):
        assert self.day.run_part("2", "test3", repeats=50) == 1464

    def test_bringup_2_4(self):
        assert self.day.run_part("2", "test3", repeats=100) == 2955

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 119

    def test_regression_2(self):
        assert self.day.run_part("2") == 21581

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
