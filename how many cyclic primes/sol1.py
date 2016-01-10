# the first one is the one i did during interview

def sol(N):
    res = 0
    sieve = [True]*(N+1)
    sieve[0] = sieve[1] = False
    for i in xrange(N+1):
        if sieve[i]:
            k = i * i
            while k <= N:
                if sieve[k]:
                    sieve[k] = False
                k += i
    primes = [i for i in xrange(len(sieve)) if sieve[i] == True]

    # this is how far i got. at first i was thinking i could solve with permutations.
    # but after wasting 5 minutes on it, i realized it wont work
    # then 30 minutes(and interview) was over
    # the rest(rest of this function and the function named rotate) i did in the next 10 minutes
    for prime in primes:
        rps = rotate(prime)
        for cyclic in rps:
            if not (cyclic in primes):
                break
        else:
            res += 1

    return res


# below is 1st attempt at optmization just after running above code. no improvement in running time

# def sol(N):
#     sieve = [True]*(N+1)
#     sieve[0] = sieve[1] = False
#     for i in xrange(N+1):
#         if sieve[i]:
#             k = i * i
#             while k <= N:
#                 if sieve[k]:
#                     sieve[k] = False
#                 k += i
#     primes = [i for i in xrange(len(sieve)) if sieve[i] == True]

#     checked = []
#     for prime in primes:
#         if not prime in checked:
#             rps = rotate(prime)
#             for cyclic in rps:
#                 if not (cyclic in primes):
#                     break
#             else:
#                 checked += rps
#     return len(checked)


def rotate(n):
    n = str(n)
    rps = set()
    rps.add(int(n))
    for i in xrange(len(n)-1):
        n = n[1:] + n[:1]
        rps.add(int(n))
    return list(rps)

def test():
    cases = [
    [1, 0],
    [10,4],
    [100, 13],
    [1000, 25],
    [100000, 43],
    # following test case could take 118 seconds in the solution that is given first(which is what I coded at the time).
    # using the second solution only takes 8 seconds.
    # [1000000, 55],
    ]
    for case,response in cases:
        print "running N={case}".format(case=case)
        result = sol(case)
        try:
            assert( result == response)
        except AssertionError:
            print "For {case}\nExpected:{response}\nGot:{result}".format(case=case, result=result, response=response)



# import profile
# profile.run("test()")

test()

