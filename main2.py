import random

def baseN(num, b=36, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
letters = 'abcdefghijklmnopqstuvwxyz'
s =  [''.join([a,b,c,d,e,f,g,h]) for a in letters for b in letters for c   in letters for d in letters for e in letters for f in letters for g in letters  for h in letters]
random.shuffle
real_password = 'aaaaaaaa'
i = 0

for code in s:
 if code == real_password:
    print()
    print('The password is:abcd ', code)
    break
 else:
    i += 1
    print(i, ' failures', end='\r')