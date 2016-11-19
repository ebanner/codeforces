import re

if __name__ == '__main__':
    n = int(raw_input())
    sched = raw_input()
    sched = re.sub(r'\s+', '', sched) # delete whitespace

    sched = re.sub(r'^0+', '', sched) # delete leading zeros
    sched = re.sub(r'0+$', '', sched) # delete trailing zeros
    sched = re.sub(r'00+', '', sched) # delete spans of contiguous strings of 2 or more zeros

    print len(sched)
