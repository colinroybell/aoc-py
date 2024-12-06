from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_21(DayBase):
    YEAR = "2015"
    DAY = "21"


def kill_rounds(hp, damage, armour):
    loss_per_turn = damage - armour
    if loss_per_turn < 1:
        loss_per_turn = 1
    return (hp + loss_per_turn -1)//loss_per_turn    



def part_a(input, part_b = False):
    tables = []
    table = None
    table_count = 0
    for line in input_generator(input):
        if table_count < 3:
            if line == "":
                tables.append(table) 
                table_count += 1
            elif "Cost" in line:
                table = []
            else:
                fields = line.split()
                new_fields = [fields[0]] + [int(n) for n in fields[1:]]
                table.append(new_fields)
        else:
            fields = line.split(':')
            num = int(fields[1])
            if fields[0] == "Hit Points":
                boss_hp = num
            elif fields[0] == "Damage":
                boss_damage = num
            else:
                boss_armour = num 

    tables[1].extend([["None",0,0,0]])
    tables[2].extend([["None",0,0,0],["None",0,0,0]])
    tables.append(tables[2])
    
    c = [None for _ in range(4)]

    best_cost = None
    for c[0] in range(0,len(tables[0])):
        for c[1] in range(0,len(tables[1])):
            for c[2] in range(0,len(tables[2])): 
                for c[3]in range(c[2]+1,len(tables[2])):
                    sum = ["",0,0,0]
                    for i in range(4):
                        sum[0] += tables[i][c[i]][0] + ', '
                        for j in range(1,4):
                            sum[j] += tables[i][c[i]][j]

                    name = sum[0]
                    cost = sum[1]
                    our_hp = 100
                    our_damage = sum[2]
                    our_armour = sum[3]

                    our_kill_rounds = kill_rounds(boss_hp, our_damage, boss_armour)
                    boss_kill_rounds = kill_rounds(our_hp, boss_damage, our_armour)

                    if our_kill_rounds <= boss_kill_rounds:
                        # We win
                        if not part_b and (best_cost == None or cost < best_cost):
                            best_cost = cost
                    else:
                        # We lose
                        if part_b and (best_cost == None or cost > best_cost):
                            best_cost = cost       

    return best_cost
        




def part_b(input):
    return part_a(input,part_b = True)


if __name__ == "__main__":
    Run_2015_21().run_cmdline()
