def getExpectedChilds(offSpring):
    expectSingle=[1, 1, 1, 3/4, 1/2, 0]

    expectChilds=list()
    for n in expectSingle:
        n = n * offSpring
        expectChilds.append(n)

    return expectChilds

if __name__=="__main__":
    offSpring = 2
    given="17073 16553 18517 18583 19946 17199"
    given=given.split(" ")
    
    genotypes=getExpectedChilds(offSpring)
    result=0
    for i in range(len(genotypes)):
        result+=float(given[i])*float(genotypes[i])

    print(result)