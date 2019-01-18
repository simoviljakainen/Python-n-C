file = input("File to set transactions on: ")
stra = "\nSTART TRANSACTION;\n"
cmmt = "\nCOMMIT;\n"

counter = 0
output = open("transaction_output.sql",  mode='a',  encoding='utf-8')
output.write(stra)

with open(file, encoding="utf-8",mode='r') as f:
    for line in f:
        counter = counter + 1
        
        if(counter%1000==0):
            output.write(cmmt+"SELECT '"+counter+" queries completed' AS '';\n"+stra)
    
        output.write(line)
        
output.write(cmmt)        
output.close()
