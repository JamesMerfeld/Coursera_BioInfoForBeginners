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
        
        
    
Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

k = 5

Profile = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],
'C': [0.4, 0.3, 0.1, 0.5, 0.1],
'G': [0.3, 0.3, 0.5, 0.2, 0.4],
'T': [0.1, 0.2, 0.1, 0.1, 0.2]}

print(ProfileMostProbablePattern(Text, k, Profile))