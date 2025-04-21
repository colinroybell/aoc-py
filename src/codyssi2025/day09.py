from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2025_09(DayBase):
    YEAR = "2025"
    DAY = "09"
    PREFIX = "codyssi"


def part_1(input, part=1):
    generator = input_generator(input)
    balances = {}
    debts = {}
    for line in generator:
        if not line:
            break
        fields = line.split()
        balances[fields[0]] = int(fields[2])
        debts[fields[0]] = []

    for line in generator:
        fields = line.split()
        debit = fields[1]
        credit = fields[3]
        amount = int(fields[5])
        if part == 2:
            amount = min(amount, balances[debit])
        if part == 3:
            if amount > balances[debit]:
                debts[debit].append([credit, amount - balances[debit]])
                amount = balances[debit]

        balances[debit] -= amount
        balances[credit] += amount
        if part == 3:
            repaid = True
            while repaid:
                repaid = False
                for a in balances.keys():
                    while len(debts[a]) > 0 and balances[a] > 0:
                        repaid = True
                        c = debts[a][0][0]
                        d = debts[a][0][1]
                        payment = min(balances[a], d)

                        balances[a] -= payment
                        balances[c] += payment
                        if payment == d:
                            debts[a] = debts[a][1:]
                        else:
                            debts[a][0][1] -= payment

    top3 = sorted(balances.items(), key=lambda x: x[1], reverse=True)[:3]

    return sum(top3[i][1] for i in range(3))


def part_2(input):
    return part_1(input, part=2)


def part_3(input):
    return part_1(input, part=3)


if __name__ == "__main__":
    Run_2025_09().run_cmdline()
