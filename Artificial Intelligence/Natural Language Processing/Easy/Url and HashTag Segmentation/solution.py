import pandas as pd

def segment_url_hashtag(text, comWordsList):
    # Segment interested text segment (Filter # or www)
    if text[0] == '#':
        rawWords = text[1:]
    elif text[:3].lower() == "www":
        ind = text.index('.', 4)
        rawWords = text[4:ind]
    else:
        ind = text.index('.')
        rawWords = text[:ind]
    
    backInd = len(rawWords)
    frontInd = 0
    segWords = []
    wordIndArr = []
    while frontInd < len(rawWords):
        if backInd == frontInd:
            if len(segWords) > 0:
                while ((wordIndArr[-1][1] - 1) == wordIndArr[-1][0]):
                    segWords = segWords[:-1]
                    wordIndArr = wordIndArr[:-1]

                frontInd = wordIndArr[-1][0]
                backInd = wordIndArr[-1][1] - 1
                segWords = segWords[:-1]
                wordIndArr = wordIndArr[:-1]
                
            else:
                segWords = [rawWords]
                break
        
        if rawWords[frontInd:backInd].lower() in comWordsList:
            segWords.append(rawWords[frontInd:backInd])
            wordIndArr.append((frontInd, backInd))
            frontInd = backInd
            backInd = len(rawWords)
        else:
            try:
                float(rawWords[frontInd:backInd])
                segWords.append(rawWords[frontInd:backInd])
                wordIndArr.append((frontInd, backInd))
                frontInd = backInd
                backInd = len(rawWords)

            except ValueError:
                backInd -= 1

    return segWords


## Main Program
commonWords = pd.read_csv('words.txt', header = None, names = ['Words'])
comWordsList = commonWords['Words'].values
comWordsList = [comWords.lower() for comWords in comWordsList]

N = int(input())
for i in range(N):
    text = input()
    segWords = segment_url_hashtag(text, comWordsList)
    print(' '.join(segWords))