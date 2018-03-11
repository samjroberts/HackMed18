import pandas as pd
import numpy as np

#Input file, database name and blast output xml
queryID="salmonella-fake.fa"
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

blast_res = df
blast_res['species'] = ''
#df[(df['Result']>=30)] #filters results to >= 30% match

df = pd.read_csv('species_annotation.csv', sep = '\t',header=-1,names = ['species','operons','GenBank','operon_length'])
df['species'] = df['species'].str.replace('_',' ')

my_file = open('operons.txt','r')

data = []

for line in my_file:
    data.append(line)

df2 = pd.DataFrame(columns=['operons','seq'],index=list(range(len(data))))


df2['data'] = data

def GetOperand(x):
    if '>' in x:
        return x

def GetSeq(x):
    if '>' not in x:
        return x

df2['operons'] = df2['data'].apply(GetOperand)
df2['seq'] = df2['data'].apply(GetSeq)
df2['operons'] = df2['operons'].ffill()
df2 = df2.dropna()
df2 = df2.drop('data',1)
df3 = df2.groupby('operons').agg(lambda x:x.tolist())
df3 = df3.reset_index()
df3['seq'] = df3['seq'].apply(lambda x:''.join(x))
df3['operons'] = df3['operons'].str.replace('>','').str.replace('\n','')


final = df3

diseases = ['amoebiasis',
            'entamoeba histolytica',
            'cryptosporidiosis',
            'cryptosporidium parvum',
            'cyclosporiasis',
            'cyclospora cayetanensis',
            'giardiasis',
            'giardia lamblia',
            'microsporidiosis',
            'microsporidia',
            'botulism',
            'clostridium botulinum',
            'campylobacteriosis',
            'camploybacter jejuni',
            'cholera',
            'vibrio cholerae',
            'e.eoli infection',
            'escherichia coli',
            'm.marinum infection',
            'mycobacterium marinum',
            'dysentery',
            'shigella dysenterae',
            'legionellosis',
            'legionella pneumophilia',
            'leptospirosis',
            'leptospira',
            'otitis externa',
            'salmonellosis',
            'salmonella',
            'typhoid fever',
            'salmonella typhi',
            'vibrio illness',
            'vibrio vulnificus',
            'vibrio alginolyticus',
            'vibrio parahaemolyticus',
            'sars',
            'coronavirus',
            'hepatitis A',
            'poliomyelitis',
            'polio',
            'poliovirus',
            'polyomavirus infection',
            'polyomavirus',
            'jc virus',
            'bk virus',
            'desmodesmus',
            'desmodesmus armatus'
            ]

full_join = pd.merge(df,final)


water_dis = full_join[full_join['species'].str.lower().isin(diseases)]

def GetInd(x):
    idx = full_join.index[full_join['operons']==x]
    return full_join['species'][idx[0]]

blast_res['species'] = blast_res['hit_id'].apply(GetInd)

blast_res_qual = blast_res[blast_res['Result']>=90]

results = (blast_res_qual.groupby('species')['hit_id'].count())
