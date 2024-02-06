import pandas as pd
from pprint import pprint


entries = pd.read_csv('no_pdb_entries.csv')
entries_found = pd.read_csv('entries_found.csv')

unfound = []

for en in entries.Entry:
    
    for x in entries_found.entry:
        
        if en != x and en not in unfound:
            unfound.append(en)
            
print(len(unfound))