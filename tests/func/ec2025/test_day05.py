import pytest
from ec2025.day05 import Run_2025_05


class Test_2025_05:
    def setup_class(self):
        self.day = Run_2025_05()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 581078

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 77053

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 260

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 4

    def test_regression_1(self):
        assert self.day.run_part("1") == 8762363643

    def test_regression_2(self):
        assert self.day.run_part("2") == 8757643946766

    def test_regression_3(self):
        assert self.day.run_part("3") == 31782246
