import math
def scientificNotation(num):
    org = num
    power = 0
    while abs(num) > 10 or abs(num)<1:
        if abs(num) > 10:
            num /= 10
            power += 1
        else:
            num *= 10
            power -= 1
    num = format(num,'.3f')
    print(str(org)+"\t=\t"+str(num)+"*10^"+str(power))

scientificNotation(10000)
scientificNotation(-11)
scientificNotation(0.342)