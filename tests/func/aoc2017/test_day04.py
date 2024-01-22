import pytest
from aoc2017.day04 import Run_2017_04, isValidPassPhrase


class Test_2017_04:
    def setup_class(self):
        self.day = Run_2017_04()

    def test_bringup_a_1(self):
        assert isValidPassPhrase("aa bb cc dd ee") == 1

    def test_bringup_a_2(self):
        assert isValidPassPhrase("aa bb cc dd aa") == 0

    def test_bringup_a_3(self):
        assert isValidPassPhrase("aa bb cc dd aaa") == 1

    def test_bringup_b_1(self):
        assert isValidPassPhrase("abcde fghij", True) == 1

    def test_bringup_b_2(self):
        assert isValidPassPhrase("abcde xyz ecdab", True) == 0

    def test_bringup_b_3(self):
        assert isValidPassPhrase("a ab abc abd abf abj", True) == 1

    def test_bringup_b_4(self):
        assert isValidPassPhrase("iiii oiii ooii oooi oooo", True) == 1

    def test_bringup_b_5(self):
        assert isValidPassPhrase("oiii ioii iioi iiio", True) == 0

    def test_regression_a(self):
        assert self.day.run_part("a") == 477

    def test_regression_b(self):
        assert self.day.run_part("b") == 167
