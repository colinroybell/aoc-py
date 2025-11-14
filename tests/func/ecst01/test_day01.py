import pytest
from ecst01.day01 import Run_st01_01


class Test_st01_01:
    def setup_class(self):
        self.day = Run_st01_01()

    @pytest.mark.skip
    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 0

    @pytest.mark.skip
    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 0

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    @pytest.mark.skip
    def test_regression_1(self):
        assert self.day.run_part("1") == 0

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
