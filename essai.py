import re

data = open("CISI.ALLnettoye","r").readlines()
data=[i[:len(i)-1] for i in data] #Enleve le '\n'
documents=[]
titles=[]
#data

#for ind in range(len(data)):
#    if ".I " in data[ind]:
#        titles.append(data[ind+1])
#titles

collection =[]
for line in range(len(data)): # Remplacer 50 par le nb de lignes au total (c'est a dire: len(data))
    if data[line].isalpha():
        doc=[]
        if data[line].split()[0]==".I":
            collection.append(doc)
        else:
            doc.append(data[line])
