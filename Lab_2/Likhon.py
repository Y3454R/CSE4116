import math
divisor=[0]*100000
prime=[]
def generate_prime():
    for i in range(4,100000,2):
        divisor[i]=1
    for i in range(3,100000,2):
        for j in range(i*2,100000,i):
            divisor[j]=1
    for i in range(2,100000,1):
        if(divisor[i]==0):
            prime.append(i)
generate_prime()

message=int(input())
p=prime[500]
q=prime[700]
n=p*q; 
phi_n=(p-1)*(q-1)

#find e
for i in range(2,phi_n):
    if(math.gcd(i,phi_n)==1):
        e=i
        break

#find d
for i in range(0,n+1):
    if((i*e)%phi_n==1):
        d=i
        break
    
def bigmod(a,b,m): #return (a^b)%m
    ans=1
    a=a%m
    while(b>0):
        if(b%2==1):
            ans=(ans*a)%m
        a=(a*a)%m
        b=b//2
    return ans

encrypted_message=bigmod(message,e,n)
print("encrypted message: ",encrypted_message)
decrypted_message=bigmod(encrypted_message,d,n)
print("decrypted message:",decrypted_message)
