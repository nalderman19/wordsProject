import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# only want words with ie/ei
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

# histogram - length of word vs how many words follow rule
# x-axis: length of word    y-axis: num of followers
# get length of word column
wordsdf['Length'] = wordsdf.Words.str.len()
# separate dataframes for true and false (for plotting purposes)
truedf = wordsdf[(wordsdf.C_Rule == True) & (wordsdf.Length <= 20)]
falsedf = wordsdf[(wordsdf.C_Rule == False) & (wordsdf.Length <= 20)]


plt.hist(x=[truedf.Length,falsedf.Length],
                            bins=np.arange(3,21,1),
                            color=['#0504aa','#d12115'],
                            alpha=0.7,
                            rwidth=0.85,
                            align='right')
plt.xlabel('Length of Word')
plt.xticks(np.arange(3,21,1))
plt.ylabel('Frequency')
plt.yticks([0,1000,2500])
plt.title('I before E rule followers based on length of word')
plt.legend(['Rule Followers','Rule Exceptions'])
plt.show()