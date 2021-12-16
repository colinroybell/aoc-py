import pytest
from aoc2021.day16 import Run_2021_16


class Test_2021_16:
    def setup_class(self):
        self.day = Run_2021_16()

    def test_bringup_a(self):
        assert self.day.run_part("a", ["D2FE28"]) == 6
        assert self.day.run_part("a", ["EE00D40C823060"]) == 14
        assert self.day.run_part("a", ["38006F45291200"]) == 9
        assert self.day.run_part("a", ["8A004A801A8002F478"]) == 16
        assert self.day.run_part("a", ["620080001611562C8802118E34"]) == 12
        assert self.day.run_part("a", ["C0015000016115A2E0802F182340"]) == 23
        assert self.day.run_part("a", ["A0016C880162017C3686B18A3D4780"]) == 31

    def test_bringup_b(self):
        assert self.day.run_part("b", ["C200B40A82"]) == 3
        assert self.day.run_part("b", ["04005AC33890"]) == 54
        assert self.day.run_part("b", ["880086C3E88112"]) == 7
        assert self.day.run_part("b", ["CE00C43D881120"]) == 9
        assert self.day.run_part("b", ["D8005AC2A8F0"]) == 1
        assert self.day.run_part("b", ["F600BC2D8F"]) == 0
        assert self.day.run_part("b", ["9C005AC2F8F0"]) == 0
        assert self.day.run_part("b", ["9C0141080250320F1802104A08"]) == 1

    def test_regression_a(self):
        assert self.day.run_part("a") == 866

    def test_regression_b(self):
        assert self.day.run_part("b") == 1392637195518
