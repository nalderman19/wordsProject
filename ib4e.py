import pandas as pd

# pass in string - return true if string contains ei or ie
def adjacent(string):
    if ('ie' in string):
        return 1
    if ('ei' in string):
        return 2
    return None

def cRule(string):
    if (('ie' in string) and (string[string.find('ie')-1] != 'c')):
        return True
    if ('cie' in string):
        return False
    if ('cei' in string):
        return True
    if ('ei' in string):
        return False

# read in txt
wordsdf = pd.read_csv('words.txt', sep='\n', skiprows=1, names=['Words'])
wordsdf['Words'] = wordsdf['Words'].astype(str)

wordsdf['Adjacent'] = list(map(adjacent, wordsdf['Words']))
wordsdf = wordsdf.dropna()
# get number of each type of eiie
numie = sum(wordsdf.Adjacent==1)
numei = sum(wordsdf.Adjacent==2)

# now check if before c is true
wordsdf['C_Rule'] = list(map(cRule, wordsdf['Words']))

# get number of words that follow c rule
numctrue = sum(wordsdf.C_Rule == True)
numcfalse = sum(wordsdf.C_Rule == False)

pctrue = numctrue / (numctrue+numcfalse)