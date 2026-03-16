import pytest
from ecst02.day01 import Run_st02_01


class Test_st02_01:
    def setup_class(self):
        self.day = Run_st02_01()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 3

    def test_bringup_1_2(self):
        assert self.day.run_part("1", "test2", trace="part1_trace1") == 26

    def test_bringup_2(self):
        assert self.day.run_part("2", "test3", trace="part2_trace1") == 115

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 48

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
