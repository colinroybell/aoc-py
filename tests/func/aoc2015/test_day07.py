import pytest
from aoc2015.day07 import Run_2015_07, Circuit


class Test_2015_07:
    def setup_class(self):
        self.day = Run_2015_07()

    def test_bringup_a(self):
        circuit = Circuit(self.day.input_filename("a", "test1"))
        assert circuit.get_value("d") == 72
        assert circuit.get_value("e") == 507
        assert circuit.get_value("f") == 492
        assert circuit.get_value("g") == 114
        assert circuit.get_value("h") == 65412
        assert circuit.get_value("i") == 65079
        assert circuit.get_value("x") == 123
        assert circuit.get_value("y") == 456

    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == 16076

    def test_regression_b(self):
        assert self.day.run_part("b") == 2797
