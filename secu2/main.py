import math
p = 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
q = 204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811
n = p*q
#print(n)
fn = (p-1)*(q-1)
#print(fN)
for i in range(2, fn):
    if (math.gcd(i, fn) == 1):
        e = i
        break
#print("e= ", e)

for k in range (0, n):
    x = 1+k*fn
    if(x%e == 0):
        d=x//e
        break
#print("d= ", d)

m = int(input("enter: "))
s = pow(m, d, n)
print("signature: ", s)
v = pow(s,e,n)
print("verification:", v)
#print(pow(s,e,n))

# 1000000000

for i in range(2, fn):
    if (math.gcd(i,fn)==1):
        e = i
        break

for i in range(0, n + 1):
    if ((i*e)%fn==1):
        d = i
        break

cTxt = pow(msg, e, n)
print("ciphertext: ", cTxt)
pTxt = pow(cTxt, d, n)
print("plaintext:", pTxt)
