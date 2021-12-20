from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2015_07(DayBase):
    YEAR = "2015"
    DAY = "07"


class Wire:
    def __init__(self, id, input, circuit):
        self.id = id
        self.value = None
        self.input = input
        self.circuit = circuit

    def get_value(self):
        if self.value:
            return self.value
        else:
            words = self.input.split(" ")
            if len(words) == 1:
                self.value = self.circuit.get_value(words[0])
            elif words[1] == "AND":
                self.value = self.circuit.get_value(words[0]) & self.circuit.get_value(
                    words[2]
                )
            elif words[1] == "OR":
                self.value = self.circuit.get_value(words[0]) | self.circuit.get_value(
                    words[2]
                )
            elif words[1] == "LSHIFT":
                self.value = (self.circuit.get_value(words[0]) << int(words[2])) & 65535
            elif words[1] == "RSHIFT":
                self.value = (self.circuit.get_value(words[0]) >> int(words[2])) & 65535
            elif words[0] == "NOT":
                self.value = 65535 - self.circuit.get_value(words[1])
        return self.value

    def reset(self):
        self.value = None

    def set_value(self, value):
        self.value = value


class Circuit:
    def __init__(self, input):
        self.wires = {}
        split_re = re.compile(r"(.+)\s->\s(.+)")
        for line in input_generator(input):
            m = split_re.match(line)
            assert m
            self.wires[m.group(2)] = Wire(m.group(2), m.group(1), self)

    def get_value(self, id):
        if id.isnumeric():
            return int(id)
        else:
            return self.wires[id].get_value()

    def reset(self):
        for _, w in self.wires.items():
            w.reset()

    def set_value(self, id, value):
        self.wires[id].set_value(value)


def part_a(input):
    circuit = Circuit(input)
    return circuit.get_value("a")


def part_b(input):
    circuit = Circuit(input)
    value = circuit.get_value("a")
    circuit.reset()
    circuit.set_value("b", value)
    return circuit.get_value("a")


if __name__ == "__main__":
    Run_2015_07().run_cmdline()
