import pytest
from ec2026.day02 import Run_2026_02


class Test_2026_02:
    def setup_class(self):
        self.day = Run_2026_02()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 122157

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 122157

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 122157

    def test_regression_1(self):
        assert self.day.run_part("1") == 450267

    def test_regression_2(self):
        assert self.day.run_part("2") == 58623407847

    def test_regression_3(self):
        assert self.day.run_part("3") == 598681826973
