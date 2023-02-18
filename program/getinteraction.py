# get genes interaction from bioGRID
# write the results to interaction.txt file
import requests
import json
#from core import config as cfg

base_url = "https://webservice.thebiogrid.org"
access_key = "bd4877a9f1e52cb13148109402830330"

request_url = base_url + "/interactions"

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
  "HTRA2"
]
#geneList = ["TMEM175", "PLA2G1"]

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/biogridrest
params = {
    "accesskey": access_key,
    "format": "tab",  # Return results in TAB2 format
    "geneList": "|".join(geneList),  # Must be | separated
    "searchNames": "true",  # Search against official names
    "includeInteractors": "true",  # Set to true to get any interaction involving EITHER gene, set to false to get interactions between genes
    "taxId": 9606,  # Limit to Homo sapiens
#    "evidenceList": "|".join(evidenceList),  # Exclude these two evidence types
#    "includeEvidence": "false",  # If false "evidenceList" is evidence to exclude, if true "evidenceList" is evidence to show
    "includeHeader": "true",
#    "excludePubmeds": "true"
}

r = requests.get(request_url, params=params)
interactions = r.text[9:]

# Pretty print out the results
#print(interactions)

filename = "../data/interactions.txt"
with open(filename, 'w') as f:
  f.write(interactions)
