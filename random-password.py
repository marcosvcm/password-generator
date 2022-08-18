import random

# from ASCII table:
# numbers: 48 -- 57
# uppercase letters: 65 -- 90
# lowercase letters: 97 -- 122 
num = [chr(x) for x in range(48, 58)]
ucl = [chr(x) for x in range(65, 91)]
lcl = [chr(x) for x in range(97, 123)]
# the special characters can be changed
sc = ['.', ',', '-', '_', '*', '!']

n = input("How many characters will the password have? ")
t = input("Whitch types of characters should the password have?\
	\n(1)numbers\n(2)lowercase letters\n(3)uppercase letters\
	\n(4)special characters\nexample of entry: 13\n")

# generating a list with the selected character types
selec = []
if '1' in t: selec += num
if '2' in t: selec += lcl
if '3' in t: selec += ucl
if '4' in t: selec += sc
if len(selec) < 1:
	t = '1'
	selec += num

pw = [selec[random.randint(0, len(selec)-1)] for x in range(int(n))]

# increasing the chances of using all the types
if '1' in t: pw[random.randint(0, len(pw)-1)] = num[random.randint(0, len(num)-1)]
if '2' in t: pw[random.randint(0, len(pw)-1)] = lcl[random.randint(0, len(ucl)-1)]
if '3' in t: pw[random.randint(0, len(pw)-1)] = ucl[random.randint(0, len(lcl)-1)]
if '4' in t: pw[random.randint(0, len(pw)-1)] = sc[random.randint(0, len(sc)-1)]

res = ""
for x in pw: res += x
print(res)

