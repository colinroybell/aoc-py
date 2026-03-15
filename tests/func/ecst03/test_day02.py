import pytest
from ecst03.day02 import Run_st03_02


class Test_st03_02:
    def setup_class(self):
        self.day = Run_st03_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 12

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 47

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test1", trace="part3_trace1") == 87

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test2", trace="part3_trace2") == 239

    def test_bringup_3_3(self):
        assert self.day.run_part("3", "test3") == 1539

    def test_regression_1(self):
        assert self.day.run_part("1") == 270

    def test_regression_2(self):
        assert self.day.run_part("2") == 3307

    def test_regression_3(self):
        assert self.day.run_part("3") == 2343
