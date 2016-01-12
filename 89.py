def fix(num): 
    num = num.replace('DCCCC','CM')
    num = num.replace('CCCC','CD')
    num = num.replace('LXXXX','XC')
    num = num.replace('XXXX','XL')
    num = num.replace('VIIII','IX')
    num = num.replace('IIII','IV')
    return num

with open('p089_roman.txt','r') as f:
    numerals = f.read().split('\n')

saved = 0

for num in numerals:
    base_size = len(num)
    fixed_size = len(fix(num))
    saved += base_size - fixed_size

print (saved)