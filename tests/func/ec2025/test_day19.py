import pytest
from ec2025.day19 import Run_2025_19


class Test_2025_19:
    def setup_class(self):
        self.day = Run_2025_19()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 24

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 22

    def test_regression_1(self):
        assert self.day.run_part("1") == 58

    def test_regression_2(self):
        assert self.day.run_part("2") == 675

    def test_regression_3(self):
        assert self.day.run_part("3") == 4314246
