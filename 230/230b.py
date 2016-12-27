import math

max_num = int(1e6) + 1

sieve = [True]*max_num
sieve[:2] = [False, False] # mark 0 and 1 as composite
for i in range(2, max_num):
    if not sieve[i]: # already marked composite
        continue

    for j in range(i*2, max_num, i):
        sieve[j] = False

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]

    for num in nums:
        a = math.sqrt(num)
        print 'YES' if int(a) == a and sieve[int(a)] else 'NO'
