import random

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
    
def Profile(Motifs):
    count = Count(Motifs)
    k = len(Motifs[0])
    t = len(Motifs)
    for symbol in "ACGT":
        for i in range(k):
            count[symbol][i] = count[symbol][i]/float(t)
    return count

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    count = 0
    consensus = Consensus(Motifs)
    for j in range(len(Motifs[0])):
        for i in range(len(Motifs)):
            if Motifs[i][j] != consensus[j]:
                count = count + 1
    return count

def Pr(Text, Profile):
    p = 1
    Text = Text.upper()
    dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p
    
def ProfileMostProbablePattern(Text, k, Profile):
    pMax = 0
    index = 0
    for i in range(len(Text)-k+1):
        kMer = Text[i:i+k]
        pTemp = Pr(kMer, Profile)
        if pTemp > pMax:
            pMax = pTemp
            index = i
    return Text[index:index+k]

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1,t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def CountWithPseudocounts(Motifs):
    count = Count(Motifs)
    for symbol in "ACGT":
        for i in range(len(count[symbol])):
            count[symbol][i] = count[symbol][i] + 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    count  = CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        for i in range(len(count[symbol])):
            count[symbol][i] = count[symbol][i]/float(t+4)
    return count

def profilePrinter(Profile):
    for symbol in "ACGT":
        print(symbol + ": " + str(Profile[symbol]))

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1,t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def Motifs(Profile, Dna):
    BestMotifs = []
    t = len(Dna)
    l = len(Profile['A'])
    for i in range(t):
        BestMotifs.append(ProfileMostProbablePattern(Dna[i], l, Profile))
    return BestMotifs

def RandomMotifs(Dna, k, t):
    RandomKmers = []
    l = len(Dna[0])
    for i in range(t):
        j = random.randint(1,l-k)
        RandomKmers.append(Dna[i][j:j+k])
    return RandomKmers

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

def Normalize(Probabilities):
    sum = 0
    for key in Probabilities:
        sum = sum + Probabilities[key]
    for key in Probabilities:
        Probabilities[key] = Probabilities[key]/float(sum)
    return Probabilities

def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    val = 0
    for key in Probabilities:
        if val < p < (val + Probabilities[key]):
            kmer = key
            break
        else:
            val = val + Probabilities[key]
    return kmer

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler(Dna, k, t, N):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    for j in range(1,N):
        i = random.randint(1,t-1)
        temp = M[i]
        profile = ProfileWithPseudocounts(M[:i]+M[i+1:])
        M[i] = ProfileGeneratedString(Dna[i], profile, k)
    if Score(M) < Score(BestMotifs):
        BestMotifs = M
    else:
        return BestMotifs