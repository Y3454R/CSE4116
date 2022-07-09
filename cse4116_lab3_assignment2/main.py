import math
# p = 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
# q = 204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811

p = 137
q = 53

n = p * q
fn = (p-1)*(q-1)

plainText = int(input("Enter your plaintext: "))

e = 2
while(e < fn):
    if (math.gcd(e, fn) == 1):
            break
    e += 1

#d = (1 / e) % fn
#d = pow(e, -1, fn)

for k in range (0, n):
    x = 1+k*fn
    if(x%e == 0):
        d=x//e
        break

c = (pow(plainText,e)) % n
decrMsg = (pow(c,d)) % n

print("e: ", e)
print("d: ", d)
print("cipher text: ", c)
print("plain text: ", decrMsg)


for i in range(100000000):
    ck = (pow(c, i))%n
    if(ck == plainText and i == d):
        print("Decryption key by attacker:", i)
        break


