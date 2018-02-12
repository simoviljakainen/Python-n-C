import random
import xlwt
import copy

s1 = [1,2,5,6]
s2 = [3,4,7,8]
s3 = [9,10,13,14]
s4 = [12,12,15,16]

t1 = [1,2,3]
t2 = [4,5,6,7]
t3 = [8,9,10,11]
t4 = [12,13,14,15,16]

#ts1 = ['Häävalssi','Hääpari leikkaa kakun','Hääpari suutelee','Hääparista kerrotaan muisto','Sulhanen vaimottelee','Joku huijaa bingossa','Sormuksia ihastellaan','Säätä kommentoidaan','Joku kehuu ruokaa','Juoma läikkyy','Jotain menee rikki','Sulhanen / morsian on hukassa','Tanssilattia täyttyy','Hääpari yllätetään','Appiukko kertoo vitsin','Joku laulaa laulun']
ts1 = ['La valse de mariage','Les epoux coupent le gateaux',"Les epoux s'embrassent",'Un souvenir est raconté sur les epoux','Le marié utilise le mot "épouse" en parlant de la mariée',"Quelqu'un triche au bingo",'On admire les alliances',"On parle du temps qu'il fait","Quelqu'un félicite le menu",'On renverse un verre','Quelque chose se casse',"Le marié ou la mariée se cherche",'La piste de dance commence à se remplir','On surprend les jeunes mariés','Le beau-père raconte une blague','Quelqu’un chante une chanson']
table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
count = 1

workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("binko")

def getRand(tb):
    
    rd = random.randint(0,3)
    while(table[tb][rd]!=0):
        rd = random.randint(0,3)
    return rd    


for n in range(0,4):

    if(n < 3):
        rd = getRand(n)
        rdt = random.randint(0,len(t1)-1)
        table[n][rd] = t1[rdt]
        del t1[rdt]
    else:
        rd = getRand(n)

        rdt = random.randint(0,len(t4)-1)
        table[n][rd] = t4[rdt]
        del t4[rdt]


    rd = getRand(n)

    rdt = random.randint(0,len(t2)-1)
    table[n][rd] = t2[rdt]
    del t2[rdt]

    rd = getRand(n)

    rdt = random.randint(0,len(t3)-1)
    table[n][rd] = t3[rdt]
    del t3[rdt]

    rd = getRand(n)

    rdt = random.randint(0,len(t4)-1)
    table[n][rd] = t4[rdt]
    del t4[rdt]

    print(n)

print(table,t1,t2,t3,t4)
temp = []
temp = copy.deepcopy(table)

table[0][2] = temp[1][0]
table[0][3] = temp[1][1]
table[1][0] = temp[0][2]
table[1][1] = temp[0][3]

table[2][2] = temp[3][0]
table[2][3] = temp[3][1]
table[3][0] = temp[2][2]
table[3][1] = temp[2][3]

print(table)
for i in range(0,4):
    for j in range(0,4):
        sheet.row(i).height_mismatch = True
        sheet.col(j).width = 256 * 20
        sheet.row(j).height = 256 * 10
        font_size_style = xlwt.easyxf('font: name MV Boli, height 220;')
        sheet.write(i, j, ts1[table[i][j]-1],font_size_style) # row, column, value

workbook.save("binko.xls") 
