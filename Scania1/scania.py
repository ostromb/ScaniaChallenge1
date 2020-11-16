import operator
def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]
"""1=+
2=-
3=/
4=x"""
numlist = [1,2,3,4,5]
numliste = [1,2,3,4,5]
hmm = perm([1,2,3,4])
vallist = [[]]
i = 0
k = 0
a = 0


while i in range(0,24):
    a = 0
    k = 0

    while k in range(0,4):
        if hmm[i][a] == 3:
            divd = operator.truediv(numlist[a],numlist[a+1])
            numlist[a] = divd
            del numlist[a+1]
            del hmm[i][a]
            a = 0
            k = 0
            while k in range(0,3):
                if hmm[i][a] == 4:
                    muld = operator.mul(numlist[a],numlist[a+1])
                    numlist[a] = muld
                    del numlist[a+1]
                    del hmm[i][a]
                    a = 0
                    k = 0
                    while k in range(0,2):
                        if hmm[i][a] == 2:
                            addd = operator.sub(numlist[a],numlist[a+1])
                            numlist[a] = addd
                            del numlist[a+1]
                            del hmm[i][a]
                            a = 0
                            k = 0
                            val = operator.add(numlist[a],numlist[a+1])
                            print(val)
                            k = 4
                            numlist = [1,2,3,4,5]
                        else:
                            a +=1
                            k +=1
                else:
                    a +=1
                    k +=1
        else:
            a += 1
            k += 1
    #print(val)
    i += 1
