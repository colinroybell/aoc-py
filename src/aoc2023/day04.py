from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2023_04(DayBase):
    YEAR='2023'
    DAY='04'


def part_a(input):
    total = 0
    for line in input_generator(input):
        stage1 = line.split(': ')[1]
        numbers = stage1.split(' | ')
        wins = numbers[0].split(' ')
        card = numbers[1].split(' ')
        score = 0
        print(line)
        for c in card:
            if c != '' and c in wins:
                print(c)
                if score == 0:
                    score = 1
                else:
                    score *= 2
        print(score)
        total += score
    return total

def part_b(input):
    total = 0
    futures = []
    for line in input_generator(input):
        if futures == []:
            count = 1
        else:
            count = futures[0]+1
            futures = futures[1:]
        stage1 = line.split(': ')[1]
        numbers = stage1.split(' | ')
        wins = numbers[0].split(' ')
        card = numbers[1].split(' ')
        score = 0
        print(line)
        print(count)
        for c in card:
            if c != '' and c in wins:
                score += 1
        for i in range(score):
            if i < len(futures):
                futures[i] += count
            else:
                futures.append(count)
        print('score',score)
        print(futures)
        total += count
    return total

if __name__ == "__main__":
    Run_2023_04().run_cmdline()
