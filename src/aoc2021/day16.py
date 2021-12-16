from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2021_16(DayBase):
    YEAR = "2021"
    DAY = "16"


class Digits:
    def __init__(self):
        self.bits = []

    def append_hex_digit(self, hex):
        v = "{:04b}".format(int(hex, 16))
        self.bits.extend([int(bit) for bit in v])

    def read_bits(self, n):
        val = 0
        for _ in range(n):
            val = val * 2 + self.bits.pop(0)
        return val


class Packet:
    next_id = 0

    def __init__(self, digits):
        self.digits = digits
        Packet.next_id += 1
        self.id = Packet.next_id
        self.bits_used = 0
        self.version = self.read_bits(3)
        self.type_id = self.read_bits(3)
        self.subpackets = []

        if self.type_id == 4:
            self.literal = 0
            cont = True
            while cont:
                cont = self.read_bits(1)
                nibble = self.read_bits(4)
                self.literal = 16 * self.literal + nibble
        else:
            self.length_type_id = self.read_bits(1)
            if self.length_type_id == 0:
                self.sub_bit_count = self.read_bits(15)
            else:
                self.sub_packets = self.read_bits(11)
            bits_used = 0
            while 1:
                if (self.length_type_id == 0 and bits_used == self.sub_bit_count) or (
                    self.length_type_id == 1
                    and len(self.subpackets) == self.sub_packets
                ):
                    break
                packet = Packet(self.digits)
                bits_used += packet.bits_used
                self.subpackets.append(packet)
            self.bits_used += bits_used

    def value(self):
        s = [p.value() for p in self.subpackets]
        if self.type_id == 0:
            return sum(s)
        elif self.type_id == 1:
            m = 1
            for v in s:
                m *= v
            return m
        elif self.type_id == 2:
            return min(s)
        elif self.type_id == 3:
            return max(s)
        elif self.type_id == 4:
            return self.literal
        elif self.type_id == 5:
            if s[0] > s[1]:
                return 1
            else:
                return 0
        elif self.type_id == 6:
            if s[0] < s[1]:
                return 1
            else:
                return 0
        elif self.type_id == 7:
            if s[0] == s[1]:
                return 1
            else:
                return 0

    def read_bits(self, n):
        self.bits_used += n
        return self.digits.read_bits(n)

    def version_sum(self):
        total = self.version
        for p in self.subpackets:
            total += p.version_sum()
        return total


def part_a(input, part_b=False):
    line = next(input_generator(input))
    digits = Digits()
    for c in line:
        digits.append_hex_digit(c)

    packet = Packet(digits)
    if part_b == False:
        return packet.version_sum()
    else:
        return packet.value()


def part_b(input):
    return part_a(input, part_b=True)


if __name__ == "__main__":
    Run_2021_16().run_cmdline()
