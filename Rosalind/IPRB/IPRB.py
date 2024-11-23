def getProb(types):
    total=sum([i for i in types.values()])
    
    DD_DD=(types["DD"]/total)*((types["DD"]-1)/(total-1))
    DR_DR=(types["DR"]/total)*((types["DR"]-1)/(total-1))
    RR_RR=(types["DR"]/total)*((types["DR"]-1)/(total-1))

    DR_DD=(types["DR"]/total)*(types["DD"]/(total-1))
    DD_DR=(types["DD"]/total)*(types["DR"]/(total-1))

    DR_RR=(types["DR"]/total)*(types["RR"]/(total-1))
    RR_DR=(types["RR"]/total)*(types["DR"]/(total-1))

    DD_RR=(types["DD"]/total)*(types["RR"]/(total-1))
    RR_DD=(types["RR"]/total)*(types["DD"]/(total-1))

    #result=1-(((DR_DR)*(1/4))+(RR_RR)+((DR_RR)*(1/2))+((RR_DR)*(1/2)))
    result=(DD_DD)+ \
           ((DR_DR)*(3/4))+ \
           (DR_DD)+ \
           (DD_DR)+ \
           ((DR_RR)*(1/2))+ \
           ((RR_DR)*(1/2))+ \
           (DD_RR)+ \
           (RR_DD)
    
    return result

if __name__=="__main__":
    types={"DD":2, "DR":2, "RR":2}
    print(getProb(types))
