# Assuming we have done something like
# pytest -n 10 -k regression and aoc -v | tee log
import re
import sys
#pass_re = re.compile(r'PASSED.+::Test_(\d+)_(\d+)::test_regression_(\s)')
pass_re = re.compile(r'PASSED.+::Test_(\d+)_(\d+)::test_regression_(.)')


filename = "log"

years = [str(x) for x in range(2015,2025)]
days = [str(x).rjust(2,'0') for x in range(1,26)]

done = {}
count = {}
total_count = 0
for year in years:
    done[year] = {}
    count[year] = 0
    for day in days:
        done[year][day] = ""

with open(filename,"r") as f:
    for line in f:
        line.rstrip()
        m = pass_re.search(line)
        if m:
            done[m.group(1)][m.group(2)] += m.group(3)
            count[m.group(1)] += 1
            total_count += 1
      
#for year in years:
#    for day in days:
#        print("{} {} {}".format(year,day,done[year][day]))            

print('<table style="background-color:cyan"><tr><th></th>')
for year in years:
    print("<th>{}</th>".format(year))        
print("</tr>")
for day in days:
    print('<tr><td>{}</td>'.format(day))
    for year in years:
        num = len(done[year][day])
        if num == 0:
            print('<td style="background-color:red"></td>')
        elif num == 1:
            print('<td style="background-color:yellow">{}</td>'.format(done[year][day]))
        else:
            print('<td style="background-color:green"></td>')
    print('</tr>')
print('<tr><td></td>')
for year in years:
    num = count[year]
    if num == 0:
        print('<td style="background-color:red">{}</td>'.format(num))
    elif num < 50:
        print('<td style="background-color:yellow">{}</td>'.format(num))
    else:
        print('<td style="background-color:green">{}</td>'.format(num))
print('</tr>')        
print('</table>')
print('<p>Total: {}</p>'.format(total_count))
