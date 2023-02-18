# organize txt file
# convert txt file to csv

import pandas as pd

filename = "interactions.txt"
df = pd.read_csv(filename, sep="\t")

#print(df.columns)
#Index(['Interaction ID', 'Entrez Gene Interactor A',
#       'Entrez Gene Interactor B', 'BioGRID ID Interactor A',
#       'BioGRID ID Interactor B', 'Systematic Name Interactor A',
#       'Systematic Name Interactor B', 'Official Symbol Interactor A',
#       'Official Symbol Interactor B', 'Synonyms Interactor A',
#       'Synonyms Interactor B', 'Experimental System',
#       'Experimental System Type', 'Author', 'Pubmed ID',
#       'Organism Interactor A', 'Organism Interactor B', 'Throughput', 'Score',
#       'Modification', 'Phenotypes', 'Qualifications', 'Tags',
#       'Source Database'],
#      dtype='object')

inter = df[['Interaction ID', 'Entrez Gene Interactor A', 'Official Symbol Interactor A', 'Entrez Gene Interactor B', 'Official Symbol Interactor B']]

inter.rename(columns={
'Entrez Gene Interactor A': 'Gene A ID',
'Official Symbol Interactor A' : 'Gene A name',
'Entrez Gene Interactor B': 'Gene B ID',
'Official Symbol Interactor B': 'Gene B name'
             }, inplace=True)

geneList = [
  "SNCA",
  "PARK2",
  "PINK1",
  "SNCAIP",
  "TMEM175",
  "DNAJC13",
  "GBA",
  "TMEM230",
  "UCHL1",
  "EIF4G1",
  "ATP13A2",
  "CHCHD2",
  "PRKAG2",
  "GIGYF2",
  "FBXO7",
  "DNAJC6",
  "PLA2G6",
  "PARK7",
  "MAPT",
  "VPS35",
  "LRRK2",
  "VPS13C",
  "SYNJ1",
  "HTRA2",
  "PTEN",
  "APP",
  "APOE",
  "BCL",
  "SQSTM1",
  "GRN"
]


# remove same gene interactions
idx = inter.index[inter['Gene A name']==inter['Gene B name']].tolist()
inter = inter.drop(idx)

# get interaction for genes in geneList
inter = inter[inter['Gene A name'].isin(geneList)]
inter = inter[inter['Gene B name'].isin(geneList)]

csvfile = "interactions.csv"
inter.to_csv(csvfile, index=False)



