import pytest
from ec2025.day17 import Run_2025_17


class Test_2025_17:
    def setup_class(self):
        self.day = Run_2025_17()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 1573

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 1090

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 592

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 330

    def test_bringup_3_3(self):
        assert self.day.run_part("3", "test5") == 3180

    def test_regression_1(self):
        assert self.day.run_part("1") == 1605

    def test_regression_2(self):
        assert self.day.run_part("2") == 66690

    def test_regression_3(self):
        assert self.day.run_part("3") == 44384
