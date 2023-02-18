# organize txt file
# convert txt file to csv

import pandas as pd

org_file = "../data/interactions_with_possible_genes.csv"
mod_file ="../data/organized.csv"

inter = pd.read_csv(org_file)
#inter = pd.read_csv(mod_file)

gene = "SNCA"

geneList = [
#  "SNCA",
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


# get one interaction only
for i in geneList:
  idx = inter[(inter['Gene A name'] == gene) & (inter['Gene B name'] == i)].head(1)
#  idx.to_csv(mod_file, mode='a', index=False, header=False)
#  print(idx)





