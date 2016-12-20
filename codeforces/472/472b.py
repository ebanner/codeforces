from collections import deque

CALL, RETURN = 'call', 'return'

def cost(F, k):
    nb_trip = len(F) / k
    if nb_trip * k < len(F):
        nb_trip += 1

    return 2*nb_trip + cost([f-1 for f in F if f-1 > 0], k) if F else 0

if __name__ == '__main__':
    n, k = [int(num) for num in raw_input().split()]
    F = [int(num)-1 for num in raw_input().split()]

    s = deque()
    s.appendleft((F, CALL))
    while s:
        data, action = s.popleft()

        if action == CALL: # function call
            F = data # unpack arguments to function call from stack

            if not F:
                # Base case:
                #
                # Because our recursion is a simple linear chain, we will
                # enounter only REUTRN cases from this point on. Hence we can
                # model the value returned from the stack as simply modifying
                # this variable.
                #
                NB_TRIP = 0 
            else:
                # Recursive case:
                #
                # Save local variables on the stack and make the recursive call.
                # Variables are saved on the stack so we can pick up where we
                # left off once we return from the recursive call..
                # 
                nb_trip = len(F) / k
                if nb_trip * k < len(F):
                    nb_trip += 1

                s.appendleft((nb_trip, RETURN))
                s.appendleft(([f-1 for f in F if f-1 > 0], CALL))

        elif action == RETURN:
            # Resume execution
            #
            # Unpack local variables we saved on the stack along with the value
            # NB_TRIP which was computed via the recursive call to finish
            # computation.
            # 
            nb_trip = data

            NB_TRIP = 2*nb_trip + NB_TRIP

    print NB_TRIP
