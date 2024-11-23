def getNucelotideProb(gcProb): 
    # GC content is equally divided in G and C
    probG = gcProb/2
    probC = probG
    # AT content (1-GC content) is equally divided in A and T
    probA = (1-gcProb)/2
    probT = probA
    
    probNuc = {'A':probA, 'T':probT, 'G':probG, 'C':probC}
    return probNuc

if __name__ == "__main__":
    # Read input
    with open('input.txt', 'r') as fr:
        reading = fr.readlines()
        # Get n (number of attempts) and x (GC probability)
        n, x = map(float, reading[0].strip().split(" "))
        # Get DNA sequence
        seq = reading[1]

    # Calculate individual nucleotide probabilities
    probNuc=getNucelotideProb(x) # get probability dictionary

    answer=False

    # Calculate probability of the entire sequence occurring
    totalProb=1
    for nuc in seq:
        prob = probNuc[nuc]
        totalProb*=prob

    # Calculate probability of sequence NOT occurring    
    complementProb = 1-totalProb 
    
    # Probability of sequence NOT occurring in n attempts
    nCaseProb = complementProb**n

    # Final probability = 1 - (probability of sequence never occurring in n attempts)
    finalProb = 1-nCaseProb 
    answer=round(finalProb, 3)

print(answer)