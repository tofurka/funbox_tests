import re
import itertools

reg_exp = "(^\[\d{4}-\d{2}-\d{2}\ \d{2}:\d{2}:\d{2}\]\ NOK$)"  
lst = [re.sub(r":\d{2}\]\ NOK$", '', line.strip()) for line in open('events.log') \
        if re.findall(reg_exp, line)]

for d, c in itertools.groupby(lst):
        print(d[1:], 'count =', len(tuple(c)))