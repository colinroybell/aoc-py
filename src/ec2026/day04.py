from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2026_04(DayBase):
    YEAR = "2026"
    DAY = "04"
    PREFIX = "ec"


def extract_n(string):
    fields = string.split("=")
    return int(fields[1])


def part_1(input):
    generator = input_generator(input)
    total = 0
    scores = {}
    for line in generator:
        values = [extract_n(s) for s in line.split(" ")]
        id = values[0]
        quest = values[1]
        part = values[2]
        time = values[3]
        if id not in scores:
            scores[id] = [0, 0]
        scores[id][1] += time
        scores[id][0] += 1

    sorted_scores = sorted(scores.items(), key=lambda item: (-item[1][0], item[1][1]))

    print(sorted_scores)
    for i in range(len(sorted_scores)):
        total += (i + 1) * sorted_scores[i][1][1]

    return total


def part_2(input):
    return part_1(input)

def get_time(times, id, quest, part):
    time = 0
    for p in range(1,part+1):
        if (quest,p) in times[id]:
            time += times[id][(quest,p)]
        else:
            return None
    return time        

def part_3(input):
    generator = input_generator(input)
    total = 0
    points = {}
    times = {}
    quests = set()
    for line in generator:
        values = [extract_n(s) for s in line.split(" ")]
        id = values[0]
        quest = values[1]
        part = values[2]
        time = values[3]
        if id not in times:
            times[id] = {}
        times[id][(quest,part)] = time    
        if id not in points:
            points[id] = 0
        quests.add(quest)

    for quest in quests:
        for part in range(1,4):
            print(f'Quest {quest}, Part {part}:')
            scores = {}
            for id in times.keys():
                time = get_time(times,id,quest,part)
                if time:
                    scores[id] = time

            sorted_scores = sorted(scores.items(), key=lambda item: item[1])

            value = 50 * part
            last_time = None
            last_value = None
            for i in range(len(sorted_scores)):    
                (id,time) = sorted_scores[i]
                if time != last_time:
                    if value <=0:
                        break
                    print(f'id={id}, time={time}, points={value}')
                    points[id] += value
                    last_time = time
                    last_value = value
                else:    
                    points[id] += last_value
                    print(f'id={id}, time={time}, points={last_value}')
                value -=1    
            print('')
    sorted_points = sorted(points.items(), key = lambda item: -item[1])
    checksum = 0
    last_score = None
    last_weight = None
    for i in range(len(sorted_points)):
        score = sorted_points[i][1]
        if score != last_score:
            checksum += (i+1) * score
            print(f'{i+1}. points={score}')
            last_score = score
            last_weight = i + 1
        else:
            print(f'{last_weight}. points={score}')
            checksum += last_weight * score    
    return checksum    

if __name__ == "__main__":
    Run_2026_04().run_cmdline()
