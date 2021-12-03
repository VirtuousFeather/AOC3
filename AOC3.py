"""
#PART 1
file = open("input.txt").read()
listOfBinary = file.split('\n')

gammaRate = []
epsilonRate = []
binaryStringG = ""
binaryStringE = ""

zeroCount1 = 0
zeroCount2 = 0
zeroCount3 = 0
zeroCount4 = 0
zeroCount5 = 0
zeroCount6 = 0
zeroCount7 = 0
zeroCount8 = 0
zeroCount9 = 0
zeroCount10 = 0
zeroCount11 = 0
zeroCount12 = 0

oneCount1 = 0
oneCount2 = 0
oneCount3 = 0
oneCount4 = 0
oneCount5 = 0
oneCount6 = 0
oneCount7 = 0
oneCount8 = 0
oneCount9 = 0
oneCount10 = 0
oneCount11 = 0
oneCount12 = 0

for characters in listOfBinary:
    separateChar = list(characters)
    if separateChar[0] == "0":
        zeroCount1 += 1
    #print(separateChar, zeroCount1, oneCount1)
    if separateChar[1] == "0":
        zeroCount2 += 1
    if separateChar[2] == "0":
        zeroCount3 += 1
    if separateChar[3] == "0":
        zeroCount4 += 1
    if separateChar[4] == "0":
        zeroCount5 += 1
    if separateChar[5] == "0":
        zeroCount6 += 1
    if separateChar[6] == "0":
        zeroCount7 += 1
    if separateChar[7] == "0":
        zeroCount8 += 1
    if separateChar[8] == "0":
        zeroCount9 += 1
    if separateChar[9] == "0":
        zeroCount10 += 1
    if separateChar[10] == "0":
        zeroCount11 += 1
    if separateChar[11] == "0":
        zeroCount12 += 1

    if separateChar[0] == "1":
        oneCount1 += 1
    if separateChar[1] == "1":
        oneCount2 += 1
    if separateChar[2] == "1":
        oneCount3 += 1
    if separateChar[3] == "1":
        oneCount4 += 1
    if separateChar[4] == "1":
        oneCount5 += 1
    if separateChar[5] == "1":
        oneCount6 += 1
    if separateChar[6] == "1":
        oneCount7 += 1
    if separateChar[7] == "1":
        oneCount8 += 1
    if separateChar[8] == "1":
        oneCount9 += 1
    if separateChar[9] == "1":
        oneCount10 += 1
    if separateChar[10] == "1":
        oneCount11 += 1
    if separateChar[11] == "1":
        oneCount12 += 1

if zeroCount1 > oneCount1:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount1 < oneCount1:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount2 > oneCount2:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount2 < oneCount2:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount3 > oneCount3:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount3 < oneCount3:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount4 > oneCount4:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount4 < oneCount4:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount5 > oneCount5:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount5 < oneCount5:
    gammaRate.append(1)
    epsilonRate.append(0)

if zeroCount6 > oneCount6:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount6 < oneCount6:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount7 > oneCount7:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount7 < oneCount7:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount8 > oneCount8:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount8 < oneCount8:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount9 > oneCount9:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount9 < oneCount9:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount10 > oneCount10:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount10 < oneCount10:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount11 > oneCount11:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount11 < oneCount11:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount12 > oneCount12:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount12 < oneCount12:
    gammaRate.append(1)
    epsilonRate.append(0)

print(gammaRate, epsilonRate)


for char in gammaRate:
    binaryStringG = binaryStringG + str(char)
print(binaryStringG)
for char in epsilonRate:
    binaryStringE = binaryStringE + str(char)
print(binaryStringE)

number1= binaryStringG
dec_number1= int(number1, 2)
print('The decimal conversion G is:', dec_number1)
number2= binaryStringE
dec_number2= int(number2, 2)
print('The decimal conversion E is:', dec_number2)

powerCon = dec_number1 * dec_number2
print("Power consumption = ",powerCon)
"""

#PART 2
file = open("input.txt").read()
listOfBinary = file.split('\n')

gammaRate = []
epsilonRate = []
binaryStringG = ""
binaryStringE = ""

zeroCount1 = 0
zeroCount2 = 0
zeroCount3 = 0
zeroCount4 = 0
zeroCount5 = 0
zeroCount6 = 0
zeroCount7 = 0
zeroCount8 = 0
zeroCount9 = 0
zeroCount10 = 0
zeroCount11 = 0
zeroCount12 = 0

oneCount1 = 0
oneCount2 = 0
oneCount3 = 0
oneCount4 = 0
oneCount5 = 0
oneCount6 = 0
oneCount7 = 0
oneCount8 = 0
oneCount9 = 0
oneCount10 = 0
oneCount11 = 0
oneCount12 = 0

for characters in listOfBinary:
    separateChar = list(characters)
    if separateChar[0] == "0":
        zeroCount1 += 1
    #print(separateChar, zeroCount1, oneCount1)
    if separateChar[1] == "0":
        zeroCount2 += 1
    if separateChar[2] == "0":
        zeroCount3 += 1
    if separateChar[3] == "0":
        zeroCount4 += 1
    if separateChar[4] == "0":
        zeroCount5 += 1
    if separateChar[5] == "0":
        zeroCount6 += 1
    if separateChar[6] == "0":
        zeroCount7 += 1
    if separateChar[7] == "0":
        zeroCount8 += 1
    if separateChar[8] == "0":
        zeroCount9 += 1
    if separateChar[9] == "0":
        zeroCount10 += 1
    if separateChar[10] == "0":
        zeroCount11 += 1
    if separateChar[11] == "0":
        zeroCount12 += 1

    if separateChar[0] == "1":
        oneCount1 += 1
    if separateChar[1] == "1":
        oneCount2 += 1
    if separateChar[2] == "1":
        oneCount3 += 1
    if separateChar[3] == "1":
        oneCount4 += 1
    if separateChar[4] == "1":
        oneCount5 += 1
    if separateChar[5] == "1":
        oneCount6 += 1
    if separateChar[6] == "1":
        oneCount7 += 1
    if separateChar[7] == "1":
        oneCount8 += 1
    if separateChar[8] == "1":
        oneCount9 += 1
    if separateChar[9] == "1":
        oneCount10 += 1
    if separateChar[10] == "1":
        oneCount11 += 1
    if separateChar[11] == "1":
        oneCount12 += 1

if zeroCount1 > oneCount1:
    
elif zeroCount1 < oneCount1:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount2 > oneCount2:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount2 < oneCount2:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount3 > oneCount3:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount3 < oneCount3:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount4 > oneCount4:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount4 < oneCount4:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount5 > oneCount5:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount5 < oneCount5:
    gammaRate.append(1)
    epsilonRate.append(0)

if zeroCount6 > oneCount6:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount6 < oneCount6:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount7 > oneCount7:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount7 < oneCount7:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount8 > oneCount8:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount8 < oneCount8:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount9 > oneCount9:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount9 < oneCount9:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount10 > oneCount10:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount10 < oneCount10:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount11 > oneCount11:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount11 < oneCount11:
    gammaRate.append(1)
    epsilonRate.append(0)
if zeroCount12 > oneCount12:
    gammaRate.append(0)
    epsilonRate.append(1)
elif zeroCount12 < oneCount12:
    gammaRate.append(1)
    epsilonRate.append(0)

print(gammaRate, epsilonRate)


for char in gammaRate:
    binaryStringG = binaryStringG + str(char)
print(binaryStringG)
for char in epsilonRate:
    binaryStringE = binaryStringE + str(char)
print(binaryStringE)

number1= binaryStringG
dec_number1= int(number1, 2)
print('The decimal conversion G is:', dec_number1)
number2= binaryStringE
dec_number2= int(number2, 2)
print('The decimal conversion E is:', dec_number2)

powerCon = dec_number1 * dec_number2
print("Power consumption = ",powerCon)