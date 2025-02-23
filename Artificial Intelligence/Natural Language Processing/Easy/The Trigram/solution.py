from sys import stdin

def extractMostFrequentNgram(text,N):
    wordsList = text.split()
    NgramList = []
    
    for ind in range(len(wordsList)-N-1):
        NgramList.append(' '.join(wordsList[ind:ind+N]))

    maxFreq = 0
    for Ngram in NgramList:
        freq = NgramList.count(Ngram)
        if freq > maxFreq:
            maxFreq = freq
            mfNgram = Ngram

    return mfNgram


## Main Program
text = ""
for line in stdin:
    text = text + line

N = 3
mfNgram = extractMostFrequentNgram(text,N)

if mfNgram[-1] == '.':
    mfNgram = mfNgram[:-1]

print(mfNgram.lower())