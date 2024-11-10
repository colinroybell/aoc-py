import pytest
from ec2024.day05 import Run_2024_05


class Test_2024_05:
    def setup_class(self):
        self.day = Run_2024_05()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1", rounds=1) == 3345

    def test_bringup_1_10(self):
        assert self.day.run_part("1", "test1", rounds=2) == 3245
        assert self.day.run_part("1", "test1", rounds=3) == 3255
        assert self.day.run_part("1", "test1", rounds=4) == 3252
        assert self.day.run_part("1", "test1", rounds=5) == 4252
        assert self.day.run_part("1", "test1", rounds=6) == 4452
        assert self.day.run_part("1", "test1", rounds=7) == 4422
        assert self.day.run_part("1", "test1", rounds=8) == 4423
        assert self.day.run_part("1", "test1", rounds=9) == 2423
        assert self.day.run_part("1", "test1", rounds=10) == 2323

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 50877075

    def test_bringup_3(self):
        assert self.day.run_part("3", "test2") == 6584

    def test_regression_1(self):
        assert self.day.run_part("1") == 2352

    def test_regression_2(self):
        assert self.day.run_part("2") == 20400801396152

    def test_regression_2(self):
        assert self.day.run_part("3") == 7591100710001003    
