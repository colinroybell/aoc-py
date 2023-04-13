import importlib
import time
from utils.day_base import DayBase

year = 2022

for day in range(1,26):
    aoc_module =  importlib.import_module("aoc{}.day{:02d}".format(year, day))
    run_object = getattr(aoc_module, "Run_{}_{:02d}".format(year, day))()
    for part in ['a', 'b']:
        start_time = time.perf_counter()
        complete = True
        try:
            res = run_object.run_part(part)
        except AssertionError:
            complete = False
        run_time = time.perf_counter() - start_time
        if complete:
            print("{}.{}.{} {} {:.3f}s".format(year,day,part,res,run_time))
        else:
            print("{}.{}.{} not done".format(year,day,part))