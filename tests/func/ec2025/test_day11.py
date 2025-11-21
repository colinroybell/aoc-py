import pytest
from ec2025.day11 import Run_2025_11


class Test_2025_11:
    def setup_class(self):
        self.day = Run_2025_11()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 109

    def test_bringup_1_checksums(self):
        checksums = [111, 114, 116, 118, 119, 121, 122, 117, 115, 113, 109]
        for round, checksum in enumerate(checksums):
            assert self.day.run_part("1", "test1", rounds=round) == checksum

    def test_bringup_2_1(self):
        assert self.day.run_part("2", "test1") == 11

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test2") == 1579

    def test_regression_1(self):
        assert self.day.run_part("1") == 213

    def test_regression_2(self):
        assert self.day.run_part("2") == 2620416

    def test_regression_3(self):
        assert self.day.run_part("3") == 128060768922277
