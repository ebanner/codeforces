def nums_generator(nums, num_len):
    """Generate permutations of length `num_length` of nums
    
    Only works with two numbers, but can be generalized by converting the number
    to base len(nums) in the for() loop.
    
    """
    for i in range(2**num_len):
        bitstring_fmt = '{0:0'+str(num_len)+'b}'
        bit_string = bitstring_fmt.format(i)
        list_nums = [nums[int(bit)] for bit in bit_string]
        str_num = ''.join(str(num) for num in list_nums)

        yield int(str_num)

def lucky_generator():
    """Generate all lucky numbers up to length 3"""

    nums = [4, 7]
    for i in range(1, 4):
        for num in nums_generator(nums, i):
            yield num

if __name__ == '__main__':
    n = int(raw_input())

    for lucky_num in lucky_generator():
        if n % lucky_num == 0:
            print 'YES'
            break
    else:
        print 'NO'
