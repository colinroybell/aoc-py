import pytest
from codyssi2025.day09 import Run_2025_09


class Test_2025_09:
    def setup_class(self):
        self.day = Run_2025_09()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 2870

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 2542

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 2511

    def test_regression_1(self):
        assert self.day.run_part("1") == 11197

    def test_regression_2(self):
        assert self.day.run_part("2") == 5746

    def test_regression_3(self):
        assert self.day.run_part("3") == 8228
