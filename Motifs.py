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
