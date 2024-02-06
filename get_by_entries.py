import pandas as pd

file = 'entries_for_search.csv' 

df = pd.read_csv(file)

unip = df[df['Dbsource'] != 'pdb']

unip.to_csv('no_pdb_entries.csv', index=False)

pdb_entries = df[df['Dbsource'] == 'pdb']

pdb_entries.to_csv('pdb_entries.csv', index=False)

print('OK')