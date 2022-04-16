def encr(plain_txt, key):
    res=""
    for i in range(0,len(plain_txt)):
        ch = plain_txt[i]
        if(ch >= 'a' and ch <= 'z'):
            x = ord(plain_txt[i]) + key - 97
            res += chr(97 + (x%26))
        elif(ch >= 'A' and ch <= 'Z'):
            x = ord(plain_txt[i]) + key - 65
            res += chr(97 + (x % 26))
        else:
            res += plain_txt[i]
    return res.upper()

plainTxt = input("Plain Text: ")
key = int(input())
cipherTxt = encr(plainTxt, key)
print("Cipher Text: " + cipherTxt)
