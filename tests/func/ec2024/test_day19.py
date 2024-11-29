import pytest
from ec2024.day19 import Run_2024_19


class Test_2024_19:
    def setup_class(self):
        self.day = Run_2024_19()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "WIN"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == "VICTORY"

    def test_regression_1(self):
        assert self.day.run_part("1") == "4144492195876552"

    def test_regression_2(self):
        assert self.day.run_part("2") == "1911628536712487"

    def test_regression_3(self):
        assert self.day.run_part("3") == "3169941163623142"
