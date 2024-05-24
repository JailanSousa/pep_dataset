import pandas as pd
import os

data = pd.read_csv('actives_pdb.csv')
for i,j in zip(data['PDB'], data['Entry']):

    url = f'https://files.rcsb.org/download/{i}.pdb'
    os.system(f'wget -O {j}.pdb {url}')