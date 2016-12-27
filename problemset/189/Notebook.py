
# coding: utf-8

# # A. Cut Ribbon
# 
# - time limit per test: 1 second
# - memory limit per test: 256 megabytes
# - input: standard input
# - output: standard output
# 
# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
# 
# - After the cutting each ribbon piece should have length a, b or c.
# - After the cutting the number of ribbon pieces should be maximum.
# - Help Polycarpus and find the number of ribbon pieces after the required cutting.
# 
# ### Input
# 
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.
# 
# ### Output
# 
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
# 
# ### Examples
# 
# input
# 
# `5 5 3 2`
# 
# output
# 
# `2`
# 
# input
# 
# `7 5 5 2`
# 
# output
# 
# `2`
# 
# #### Note
# In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.
# 
# In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.

# ### Standard Input Generator

# In[27]:

import sys

# ### Generator to Read in Examples

# In[28]:

def example_generator(line):
    """Read example from stdin and parse it into the appropriate data structure
    
    Use in the following way:
    
    example = example_generator(stdin_generator)
    while True:
        numbers, target = next(example)
        .
        .
        .
    
    """
    while True:
         n, a, b, c = [int(num) for num in next(line).split()]
         
         yield n, a, b, c


# ### Workhorse Functions

# In[29]:

def do_ribbon(n, a, b, c):
    """Find the maximum number of parts a ribbon of length n can be cut into
    
    Each part has to be of length either a, b, or c.
    
    Use dynamic programming!
    
    """
    dp = [0]*(n+1)

    # Guard against chunk sizes that will never be small enough to cut the ribbon
    chunk_sizes = [val for val in [a, b, c] if val <=n]
    
    # Initial dp step
    for chunk_size in chunk_sizes:
        dp[chunk_size] = 1
        
    for i in range(1, n):
        if not dp[i]:
            continue # zero ways to cut up this ribbon evenly
            
        for chunk_size in chunk_sizes:
            if i + chunk_size > n:
                continue # don't consider values off the end of the dp table
                
            dp[i+chunk_size] = max(dp[i]+1, dp[i+chunk_size])
            
    print(dp[n])


# ### Main Loop

# In[30]:

if __name__ == '__main__':

    example = example_generator(sys.stdin)

    n, a, b, c = next(example)
    do_ribbon(n, a, b, c)
