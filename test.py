import pandas as pd


df = pd.read_csv('species_annotation.csv', sep = '\t',header=-1,names = ['species','operons','GenBank','operon_length'])
df['species'] = df['species'].str.replace('_',' ')

# %%

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

# %%

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

# %%
water_dis = full_join[full_join['species'].str.lower().isin(diseases)]
