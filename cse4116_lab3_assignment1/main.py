import math
p = 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
# q = 204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811
#
# n = p*q
# fn = (p-1)*(q-1)
#
# e = 2
# while(e < fn):
#     if (math.gcd(e, fn) == 1):
#             break
#     e += 1
#
# for i in range(0, n):
#     x = 1 + (i*fn)
#     if(x%e == 0):
#         d = x//e
#         break
#
# print("e: ", e)
# print("d: ", d)
#
# msg1 = int(input("enter msg1: "))
# msg2 = int(input("enter msg2: "))
#
# print("msg1 * msg2: ", msg1*msg2)
# c1 = pow(msg1, e, n)
# c2 = pow(msg2, e, n)
#
# print("c1: ", c1)
# print("c2: ", c2)
# print("c: ", c1*c2)
#
#
#
# decr = pow(c1*c2, d, n)
# print("decrypted: ", decr)
