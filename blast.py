import pandas as pd
import numpy as np

#Input file, database name and blast output xml
queryID="readst.txt"
dbID="operons.100.fa"
outputID="out.xml"

#Biopython runs blast through the command line
from Bio.Blast.Applications import NcbiblastnCommandline
blastn_cline = NcbiblastnCommandline(query=queryID,db =dbID,
                                     outfmt=5, out=outputID)

stdout, stderr = blastn_cline()

#This section processes the information from the blast xml output into something useful.
#Using element tree package to retrieve relevent xml information
import xml.etree.ElementTree as ET
tree = ET.parse(outputID)
root = tree.getroot()

df = pd.DataFrame(columns=['hit_id','e_value', 'Hsp_score', 'Hit_len'])

#Builds xml data into dataframe
j=0
iterator=root.iter('Hit_id')
for i in iterator:
    df.loc[j] = i.text
    j+=1
k = 0
iterator=root.iter('Hsp_evalue')
for i in iterator:
    df['e_value'].loc[k] = i.text
    k+=1

l = 0
iterator=root.iter('Hsp_score')
for i in iterator:
    df['Hsp_score'].loc[l] = i.text
    l+=1

m = 0
iterator=root.iter('Hit_len')
for i in iterator:
    df['Hit_len'].loc[m] = i.text
    m+=1

#Calculates percentage read match and filters result
df['Hsp_score'] = pd.to_numeric(df['Hsp_score'])#converts string to number
df['Hit_len'] = pd.to_numeric(df['Hit_len'])#converts string to number
df['Result'] = df['Hsp_score']/df['Hit_len']*100
df[(df['Result']>=30)] #filters results to >= 30% match
