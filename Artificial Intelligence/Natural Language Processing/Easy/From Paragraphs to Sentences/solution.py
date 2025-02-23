def segment_sentences(text):
    sent_closer = [".", '?', "!"]
    sent_list = []
    wordStart = True
    isFirstLetterCap = False
    isQuoteStart = False
    isQuoteCloser = False
    sentence = ""
    for ind in range(len(text)):
        if text[ind].isalpha():
            if wordStart:
                if text[ind].lower() != text[ind]:
                    isFirstLetterCap = True
                    if isQuoteCloser: #Miscellaneous Case Check: When after quotation, starts with caps.
                        sent_list.append(sentence)
                        sentence = ""
                else:
                    isFirstLetterCap = False
                isQuoteCloser = False
                wordStart = False
                wordLength = 1
            else:
                wordLength += 1
            sentence += text[ind]
        else:   # If detected any special characters
            if not ((len(sentence) == 0) and (text[ind] == " ")):
                sentence += text[ind]
            wordStart = True
            if text[ind] in ["\"","\'"]:
                if not (text[ind] == "\'" and (text[ind-1].isalpha() and text[ind+1].isalpha())): # Apostrophe Check
                    if isQuoteStart:
                        isQuoteStart = False
                    else:
                        isQuoteStart = True

            if text[ind] in sent_closer:
                if not isQuoteStart:    # Quotation Check
                    if not ((text[ind] == ".") and (isFirstLetterCap) and (wordLength < 3)):    # Abbreviation Check
                        sent_list.append(sentence)
                        sentence = ""
                else:
                    isQuoteCloser = True

    return sent_list


## Main Program
textChunk = input()

sent_list = segment_sentences(textChunk)

for sentence in sent_list:
    print(sentence)