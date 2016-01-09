# this is second attempt at optimization
# this took 20 minutes as I already knew what i need to do.
def sol(N):
    count_cyclic_primes = 0
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in xrange(N+1):
        if sieve[i]:
            k = i*i
            while k <= N:
                if sieve[k]:
                    sieve[k] = False
                k += i
    primes = [i for i in xrange(N+1) if sieve[i]]
    for prime in primes:
        if cycle_prime_check(prime, sieve):
            count_cyclic_primes += 1
    return count_cyclic_primes

# this function is where all the improvement is.
# instead of returning list of rotations, it checks if rotation is prime and if not immediately returns
def cycle_prime_check(n,sieve):
    N = n
    n = str(n)
    for i in xrange(N-1):
        n = n[1:]+n[:1]
        if not sieve[int(n)]:
            break
    else:
        return True
    return False


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

