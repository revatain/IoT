'''
파일명 : ex2.py
개발자 : DJJung
'''

ss = ''
ss = input('입력 문자열 ==> ')
# print('출력문자열 ==> %s' % ss, end='')

if ss.startswith('(') == False:
    print('(',end='')

print(ss, end='')

if ss.endswith(')') == False:
    print(')',end='')

inStr = '    한글 Python 프로그래밍    '
outStr = ''
outStr = inStr.replace(' ', '')
print("\n %s" % inStr)
print("%s" % outStr)

outStr = ''
for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr+=inStr[i]
print("원래 문자열 : [%s]" % inStr)
print("공백제거 문자열 : [%s]" % outStr)










