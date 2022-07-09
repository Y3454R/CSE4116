import math

#p = 96192759682482136361283586897480020521087875967458251803173219241271230713408783056720392924724665501252020941604287048896677210643120613751471976510767 
#q = 7994412097716110548127211733331600522933776757046707649963673962686200838432950239103981070728369599816314646482720706826018360181196843154224748382211019


p = 47
q = 53

n = p * q
phin = (p-1)*(q-1)

plainText = int(input("Enter your plaintext: "))
e = 2

while(e < phin):
    if (math.gcd(e, phin)==1):
            break
    e+=1

d = pow(e,-1,phin)

#d = (1 / e) % phin



encrypted = (pow(plainText,e)) % n
decrypted = (pow(encrypted,d)) % n

print("Encryption key: ", e)
print("Decryption key: ", d)
print("Encrypted message: ", encrypted)
print("Decrypted message: ", decrypted)


for i in range(10000):
    D = (pow(encrypted,i))%n
    if(D==plainText):
        print("Decryption key:",i)