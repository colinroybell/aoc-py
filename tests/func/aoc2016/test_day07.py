import pytest
from aoc2016.day07 import Run_2016_07,tls,ssl


class Test_2016_07:
    def setup_class(self):
        self.day = Run_2016_07()

    def test_bringup_a(self):
        assert tls("abba[mnop]qrst")
        assert not tls("abcd[bddb]xyyx")
        assert not tls("aaaa[qwer]tyui")
        assert tls("ioxxoj[asdfgh]zxcvbn")

    def test_bringup_b(self):
        assert ssl("aba[bab]xyz")
        assert not ssl("xyx[xyx]xyx")
        assert ssl("aaa[kek]eke")
        assert ssl("zazbz[bzb]cdb")

    def test_regression_a(self):
        assert self.day.run_part("a") == 118

    def test_regression_b(self):
        assert self.day.run_part("b") == 260
