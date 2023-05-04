sWind = 0
pWind = 0
#function to find the longest common string in  search string according to the search window
def longest_common_substring(s1, s2):
    Mxlngst= 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (Mxlngst< longest):
                        Mxlngst= longest
                        offset = i
                else:
                    break
            else:
                break
    return   Mxlngst, offset
#funtion is to encode the message signal
def encode_lz77(text, sWind, pWind):
    encodnu = [] #length of message
    encdsize = [] #encodednumber is the size of message 
    encdletr = []#letter to encode
    i = 0
    while i < len(text):
        if i < pWind:
            encodnu.append(0)
            encdsize.append(0)
            encdletr.append(text[i])
            i = i + 1
        else:
            prstring = text[i:i+pWind]
            srWindwOfset = 0
            if (i < sWind):
                srWindwOfset = i
            else:
                srWindwOfset = sWind
            searchString = text[i - srWindwOfset:i]
            reslt = longest_common_substring(searchString + prstring, prstring) #find the longest common string in window search string + preview string
            nxtlttr= ''
            if (reslt[0] == len(prstring)):
                if (i + reslt[0] == len(text)):
                    nxtlttr= ''
                else:
                    nxtlttr= text[i+pWind]
            else:
                nxtlttr= prstring[reslt[0]]
            if (reslt[0] == 0):
                encodnu.append(0)
                encdsize.append(0)
                encdletr.append(nxtlttr)
            else:
                encodnu.append(srWindwOfset - reslt[1])
                encdsize.append(reslt[0])
                encdletr.append(nxtlttr)
            i = i + reslt[0] + 1
    return encodnu, encdsize, encdletr
#function to decode the compressed message
def decode_lz77(encodnu, encdsize, encdletr):
    i = 0
    decodedString = []
    while i < len(encodnu):
        if (encodnu[i] == 0):
            decodedString.append(encdletr[i])
        else:
            currentSize = len(decodedString)
            for j in range(0, encdsize[i]):
                decodedString.append(decodedString[currentSize-encodnu[i]+j])
            decodedString.append(encdletr[i])
        i = i+1
    return decodedString



print("string to encode is 1001100111100101010100101010010110111001110101111010110101000101111001011111110011010011011001111")
strngTEncd ="1001100111100101010100101010010110111001110101111010110101000101111001011111110011010011011001111"
print("searchWindow is 10")
print("previewWindow is 5")
sWind = 10
pWind = 5
[encodnu, encdsize, encdletr] = encode_lz77(strngTEncd, sWind, pWind)
a =[encodnu, encdsize, encdletr]
i = 0
while i < len(encodnu):
    print ("{",encodnu[i],":", encdsize[i],":", encdletr[i],"}",end = " ")
    i = i + 1
print("\n")
decodedString = decode_lz77(encodnu, encdsize, encdletr)
print("Decoded string:", "".join(decodedString))
