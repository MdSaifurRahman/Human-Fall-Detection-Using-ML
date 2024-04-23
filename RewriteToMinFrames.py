import math
file=open('data1.txt','r')
lines=file.readlines()
data=[]
minCount=math.inf
for i in lines:
    j=i.split(' ')
    j[-1]=j[-1][:-1]
    data.append(j)
    print(len(j))
    if len(j)<minCount:
        minCount=len(j)
# print(data)
print("mincount",minCount)

# *****writing to file**
writeFile=open('test111DataMin.txt','w')
print(minCount)
for line in data:
    for i in range(len(lines)-minCount,len(lines)):
        writeFile.write(line[i])
        if i!=minCount-1:
            writeFile.write(' ')
    writeFile.write('\n')

    


