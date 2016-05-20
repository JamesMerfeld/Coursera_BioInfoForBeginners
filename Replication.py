# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
                count = count+1
    return count
    
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

Text1 = "ATGATCAAG"
Text2 = "CTTGATCAT"
Text3 = "TCTTGATCA"
Text4 = "CTCTTGATC"
print(Text1)
print(ReverseComplement(Text2))
print(Text2)
print(ReverseComplement(Text1))