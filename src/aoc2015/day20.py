from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_20(DayBase):
    YEAR = "2015"
    DAY = "20"

def value(cand,primes):
    v = 1
    for i in range(len(cand)):
        v *= (primes[i]**(cand[i]+1)-1)//(primes[i]-1)
    return v    

class RecordList:
    def __init__(self, items):
        self.items = items 

    def copy(self): 
        return RecordList(self.items.copy())

    def try_add(self, item):
        (n,v,_) = item
        last_item = self.items[-1]
        if n > last_item[0]:
            if v > last_item[1]:
                self.items.append(item)
                return True
            else:
                return False
        i = 0
        while self.items[i+1][0] < n:
            i += 1
        # number between i and i+1    
        if v < self.items[i][1]:
            return False
        # Add to position i+1
        self.items = self.items[:i+1] + [item] + self.items[i+1:]
        j = i + 2
        while j < len(self.items) and self.items[j][1] < v:        
            j += 1
        self.items = self.items[:i+2] + self.items[j:] 
        return True   

def part_a(input):
    target = int(next(input_generator(input)))//10

    primes = [2,3,5,7,11,13,17,19]
    record_list = RecordList([(1,1,[])])
    for i,p in enumerate(primes):
        change = False
        new_record_list = record_list.copy()
        for (r,v,f_in) in record_list.items:
            fact = f_in.copy()
            fact.extend([0]*(i+1-len(fact)))
            while v < target:
                r *= p
                fact[-1] += 1
                v = value(fact, primes) 
                update = new_record_list.try_add((r,v,fact.copy()))
                print(new_record_list.items)
                if update:
                    change = True
        record_list = new_record_list            
        if not change:
            break
    for (r,v,_) in record_list.items:
        if v > target:
            return r
        
# TODO: is there a nice way of doing this?        

def part_b(input):
    target = int(next(input_generator(input)))
    i = 1
    while 1:
        score = 0
        for n in range(1,51):
            if i%n == 0:
                score += 11*(i//n)
        if score > target:
            return i        
        else:
            i+=1

    


if __name__ == "__main__":
    Run_2015_20().run_cmdline()
