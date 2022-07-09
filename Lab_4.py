import Crypto.Util.number as num
import random
from math import sqrt

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def power(x, y, p):
    res = 1 

    x = x % p 

    while (y > 0):

        if (y & 1):
            res = (res * x) % p

        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def findPrimefactors(s, n):
    
    while (n % 2 == 0):
        s.add(2)
        n = n // 2

    for i in range(3, int(sqrt(n)), 2):

        while (n % i == 0):
            s.add(i)
            n = n // i

    if (n > 2):
        s.add(n)



def findPrimitive(n):
    s = set()

    if (isPrime(n) == False):
        return -1

    phi = n - 1

    findPrimefactors(s, phi)

    for r in range(2, phi + 1):

      
        flag = False
        for it in s:

            if (power(r, phi // it, n) == 1):
                flag = True
                break

        if (flag == False):
            return r
            
    return -1


def egKey(s):
    p = 1000000007
    a = findPrimitive(p);
    x = random.randint(1, p - 2)
    y = pow(a, x, p)
    return p, a, x, y


#Signature Generation 


def sigGen(p, a, x, m):
    while 1:
        k = random.randint(1, p - 2)
        if num.GCD(k, p - 1) == 1:
            break
    r = pow(a, k, p)
    l = num.inverse(k, p - 1)
    s = l * (m - x * r) % (p - 1)
    return r, s


#Signature verification


def sigVer(p, a, y, r, s, m):
    if (r < 1 or r > p - 1):
      return False
    v1 = pow(y, r, p) % p * pow(r, s, p) % p
    v2 = pow(a, m, p)
    print("v1: ", v1)
    print("v2: ", v2)
    return v1 == v2


message = 545
print ("Message: ", message)
prime, alpha, private, public = egKey(10)
print ("prime,alpha,private,public: ", prime, alpha, private, public)
y1, y2 = sigGen(prime, alpha, private, message)
print ("y1, y2: ", y1, y2)
isValid = sigVer(prime, alpha, public, y1, y2, message)
print ("Valid Signature: ", isValid)