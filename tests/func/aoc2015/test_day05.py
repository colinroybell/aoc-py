import pytest
from aoc2015.day05 import Run_2015_05, nice, nice_b


class Test_2015_05:
    def setup_class(self):
        self.day = Run_2015_05()

    def test_bringup_a(self):
        assert nice("ugknbfddgicrmopn")
        assert nice("aaa")
        assert not nice("jchzalrnumimnmhp")
        assert not nice("haegwjzuvuyypxyu")
        assert not nice("dvszwmarrgswjxmb")

    def test_bringup_b(self):
        assert nice_b("qjhvhtzxzqqjkmpb")
        assert nice_b("xxyxx")
        assert not nice_b("uurcxstgmygtbstg")
        assert not nice_b("ieodomkazucvgmuy")

    def test_regression_a(self):
        assert self.day.run_part("a") == 238

    def test_regression_b(self):
        assert self.day.run_part("b") == 69
