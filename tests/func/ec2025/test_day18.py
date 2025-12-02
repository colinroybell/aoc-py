import pytest
from ec2025.day18 import Run_2025_18


class Test_2025_18:
    def setup_class(self):
        self.day = Run_2025_18()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 774

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 324

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 946

    def test_regression_1(self):
        assert self.day.run_part("1") == 3924233

    def test_regression_2(self):
        assert self.day.run_part("2") == 17421519022

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
