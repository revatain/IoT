# ex2.py

a = ord('a')
print(a)

a = ord('A') #65
mask = 0x0F #15 , 0000 1111

print("%x & %x = %x" %(a, mask, a&mask)) #%x는 16진수
print("%x | %x = %x" %(a, mask, a|mask))

mask = ord('a')-ord('A')
# print(mask) #32

b = a ^ mask
print("%c ^ %d = %c" %(a,mask, b)) # %c 문자
a = b ^ mask
print("%c ^ %d = %c" %(b,mask, a))