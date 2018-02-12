## FileSplitter 1.0 ##

file = input("File to be split: ")
lines = input("How many lines/file: ")
output = input("Output file name: ")

lc = 1
fc = 1
tempStr = ""

with open(file,encoding='latin-1') as f:
    for line in f:
        tempStr = tempStr + line;
        lc = lc +1
        if(lc%int(lines)==0):
            strk = output + str(fc) + '.txt'
            outFile = open(strk,  mode='w',  encoding='latin-1')
            outFile.write(tempStr)
            outFile.close()
            fc = fc+1
            tempStr = ""

outFile = open(output+str(fc)+".txt", mode="w",  encoding="latin-1")
outFile.write(tempStr)
outFile.close()
