# -*- coding: utf-8 -*-

import pandas as pd
import re
import os
import nltk
from nltk import *

path = "C://Users/admin/Desktop/Raghav/Syracuse University/Semester 2/IST 664 Natural Language Processing/Assignment 2/Data for HW2/"
filelist = os.listdir(path)
x6 = list()

# Apply regular expression on all the reports 
for i in filelist:
    with open(path + i, 'r') as f:
        rawtext = f.read()
        a = re.compile('[\s]{2,}')
        rawtext = a.sub(" ",rawtext)
        pword = re.compile('[F]ile\s:\s[a]\d+|[O]rg\s:\s[A-Z]{3,4}\s|\$+\d+|[A]bstract\s:\s[\(|\|")]*[0-9]*\w+.*\w+')
        g = re.findall(pword,rawtext)
        g = [s.replace("Abstract : ","") for s in g]
        g = [s.replace("Org : ","") for s in g]
        g = [s.replace("File : ","") for s in g]
        x6.append(g)
        
df0 = pd.DataFrame(x6)        
pd.set_option('display.width', 1000)
#df0[:50]

t = ""
for index,row in df0.iterrows():
    if df0.iloc[index,1] is not None:
        t = t + df0.iloc[index,1] + '\t' + df0.iloc[index,0] + '  '+ df0.iloc[index,2] + '   '+ df0.iloc[index,3][:990] + '\n'

# Write the output as a text file
f = open("part1.txt","w")
f.write(t)
f.close()

# Import the output as csv from Data Frame
from pandas import ExcelWriter
writer = ExcelWriter('Part1.xlsx')
df0.to_excel(writer,'Sheet5')
writer.save()
df0.to_csv('Part1.csv', sep = ',')

g = ""
# Print sentences from all the abstracts
g = "Abstract_ID" + "|" + "Sentence_No" + "|" + "Sentence" '\n' + "--------------------------------------"
for index,row in df0.iterrows():
     j = nltk.sent_tokenize(str(df0.iloc[index,-1]))
     k = len(j)
     for l in range(0, k):
         if df0.iloc[index,1] is not None:
             g = g + '\n' + df0.iloc[index,1] + '|' + str(l+1) + '|'+ j[l]
     if df0.iloc[index,1] is not None:
        g = g + '\n' + "Number of sentences: " + str(l+1)
         
# Write the output as a text file        
f = open("part2.txt","w")
f.write(g)
f.close()     
     