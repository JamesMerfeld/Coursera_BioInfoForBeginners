# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
                count = count+1
    return count

# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:       
            positions.append(i)
    return positions
    
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentrevComps = [] # output variable
    Count = CountDict(Text,k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentrevComps.append(Text[i:i+k])
    FrequentrevCompsNoDuplicates = remove_duplicates(FrequentrevComps)
    return FrequentrevCompsNoDuplicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
    for item in Items:
        if not item in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {} 
    for i in range(len(Text)-k+1):
        revComp = Text[i:i+k]
        Count[i] = revCompCount(revComp, Text)
    return Count

# Input:  Strings revComp and Text
# Output: The number of times revComp appears in Text
def revCompCount(revComp, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(revComp)+1):
        if Text[i:i+len(revComp)] == revComp:
                count = count+1
    return count

def Reverse(Text):
    newText = ''
    i = len(Text)-1
    while(i >= 0):
        newText = newText + Text[i]
        i = i - 1
    return newText

def ReverseComplement(Pattern):
    revComp = list(Reverse(Pattern))
    for i in range(0,len(revComp)):
        if (revComp[i] == "A"):
            revComp[i] = 'T'
        elif (revComp[i] == "a"):
            revComp[i] = 't'
        elif (revComp[i] == "T"):
            revComp[i] = 'A'
        elif (revComp[i] == "t"):
            revComp[i] = 'a'
        elif (revComp[i] == "C"):
            revComp[i] = 'G'
        elif (revComp[i] == "c"):
            revComp[i] = 'g'
        elif (revComp[i] == "G"):
            revComp[i] = 'C'
        elif (revComp[i] == "g"):
            revComp[i] = 'c'
        else:
            print("Error:Invalid Character")
    return "".join(revComp)
    
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1,n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
    
def Skew(Genome):
    skew = {}
    n = len(Genome)
    skew[0] = 0
    for i in range(1,n+1):
        skew[i] = skew[i-1]
        if Genome[i-1] == "G":
            skew[i] = skew[i]+1
        elif Genome[i-1] == "C":
            skew[i] = skew[i]-1
    return skew
    
def MinimumSkew2(Genome):
    array = Skew(Genome).values()
    minimum = array.index(min(array))
    positions = []
    for i in range(len(array)):
        if array[i] == array[minimum]:
            positions.append(i)
    return positions
        
def MinimumSkew(Genome):
    array = list(Skew(Genome).values())
    minimum = min(array)
    positions = []
    for i in range(len(array)):
        if array[i] == minimum:
            positions.append(i)
    return positions

def HammingDistance(p,q):
    distance = 0
    if (len(p) != len(q)):
        print("ERROR: Input string must be of the same length")
        return len(p)+len(q)
    for i in range(len(p)):
        if (p[i] != q[i]):
            distance = distance + 1 
    return distance
    
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern,Text[i:i+len(Pattern)]) <= d:
            positions.append(i)
    return positions
    
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
                count = count+1
    return count
