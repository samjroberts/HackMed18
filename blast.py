import pandas as pd
import numpy as np

from Bio.Blast.Applications import NcbiblastnCommandline
blastn_cline = NcbiblastnCommandline(query="readst.txt",db ="operons.100.fa",
                                     outfmt=5, out="out.xml")
#blastn_cline
stdout, stderr = blastn_cline()

import xml.etree.ElementTree as ET
tree = ET.parse('out.xml')
root = tree.getroot()

df = pd.DataFrame(columns=['hit_id','e_value', 'Hsp_score', 'Hit_len'])

# df.fillna(value=np.nan)
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

df['Hsp_score'] = pd.to_numeric(df['Hsp_score'])
df['Hit_len'] = pd.to_numeric(df['Hit_len'])
df['Result'] = df['Hsp_score']/df['Hit_len']*100
df[(df['Result']>=30)]
