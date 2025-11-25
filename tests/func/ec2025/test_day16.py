import pytest
from ec2025.day16 import Run_2025_16


class Test_2025_16:
    def setup_class(self):
        self.day = Run_2025_16()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 193

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 270

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2",blocks=1) == 1
        assert self.day.run_part("3", "test2",blocks=2) == 1
        assert self.day.run_part("3", "test2",blocks=3) == 2
        assert self.day.run_part("3", "test2",blocks=10) == 5
        assert self.day.run_part("3", "test2",blocks=100) == 47
        assert self.day.run_part("3", "test2") == 94439495762954

    def test_regression_1(self):
        assert self.day.run_part("1") == 238

    def test_regression_2(self):
        assert self.day.run_part("2") == 168901189632

    def test_regression_3(self):
        assert self.day.run_part("3") == 95233598287935
