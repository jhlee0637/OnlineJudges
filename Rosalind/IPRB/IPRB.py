'''
https://rosalind.info/problems/iprb/

Problem: Probability is the mathematical study of randomly occurring phenomena.
         
         We will model such a phenomenon with a random variable,
         which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

         For example, say that we have a bag containing 3 red balls and 2 blue balls.
         
         If we let X represent the random variable corresponding to the color of a drawn ball,
         then the probability of each of the two outcomes is given by Pr(X=red)=3/5 and Pr(X=blue)=2/5.
 
         Random variables can be combined to yield new random variables.
         
         Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball).
 
         The probability of Y being red depends on whether the first ball was red or blue.
         
         To represent all outcomes of X and Y, we therefore use a probability tree diagram.
         
         This branching diagram represents all possible individual probabilities for X and Y,
         with outcomes at the endpoints ("leaves") of the tree.
         
         The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

         An event is simply a collection of outcomes.
         
         Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes.
         
         For our colored ball example, let A be the event "Y is blue."
          
         Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 3/10+1/10=2/5 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
       k individuals are homozygous dominant for a factor,
       m are heterozygous,
       and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype).
        Assume that any two organisms can mate.

Sample Dataset: 2 2 2

Sample Output: 0.78333
'''
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
    types={"DD":24, "DR":26, "RR":30}
    print(getProb(types))
