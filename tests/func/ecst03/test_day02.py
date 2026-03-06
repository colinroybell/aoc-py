import pytest
from ecst03.day02 import Run_st03_02


class Test_st03_02:
    def setup_class(self):
        self.day = Run_st03_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 12

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 47

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 270

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
