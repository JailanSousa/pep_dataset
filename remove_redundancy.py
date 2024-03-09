import pandas as pd
import os

#os.chdir('/home/jssousa/pep_dataset/datasets')

file = 'search_accession.csv'

df = pd.read_csv(file)

#df_non_redundante = df.drop_duplicates(subset=['sequence'], keep='first')

#df_non_redundante.to_excel('keep_first_non_redundant_pepset_uniprot_end_ncbi.xlsx', index=False)

df_non_redd = df.drop_duplicates(subset=['Entry'], keep='first')

df_non_redd.to_csv('search_accession.csv', index=False)

print('OK')