import pytest
from ec2024.day02 import Run_2024_02


class Test_2024_02:
    def setup_class(self):
        self.day = Run_2024_02()

    def test_bringup_1_1(self):
        assert self.day.run_part("1", "test1") == 4

    def test_bringup_1_2(self):
        assert (
            self.day.run_part(
                "1", "test1", phrase="THE FLAME SHIELDED THE HEART OF THE KINGS"
            )
            == 3
        )

    def test_bringup_1_3(self):
        assert self.day.run_part("1", "test1", phrase="POWE PO WER P OWE R") == 2

    def test_bringup_1_4(self):
        assert self.day.run_part("1", "test1", phrase="THERE IS THE END") == 3

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 37

    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 10

    def test_regression_1(self):
        assert self.day.run_part("1") == 36

    def test_regression_2(self):
        assert self.day.run_part("2") == 5225

    def test_regression_3(self):
        assert self.day.run_part("3") == 11305
