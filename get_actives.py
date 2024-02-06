import pandas as pd
from tqdm import tqdm

pepset = pd.read_csv('pep_dataset_filted.csv')

actives = []
for seq in tqdm(pepset.values):
    
    if 'VGSC' in seq[-2] or 'Nav' in seq[-2]:
        
        act = {
            'Entry': seq[0],
            'pdb_code': seq[1],
            'Sequence': seq[2],
            'lenght': seq[3],
            'kindom': seq[4],
            'organism': seq[5],
            'protein_name': seq[7],
            'PubMed': seq[8],
            'function': seq[10],
            'short_function': seq[11],
            'keep': 1
            }
    elif 'VGSC' not in seq[-2] or 'Nav' not in seq[-2]:
        
        act = {
            'Entry': seq[0],
            'pdb_code': seq[1],
            'Sequence': seq[2],
            'lenght': seq[3],
            'kindom': seq[4],
            'organism': seq[5],
            'protein_name': seq[7],
            'PubMed': seq[8],
            'function': seq[10],
            'short_function': seq[11],
            'keep': 0
            }
    actives.append(act)
        
df = pd.DataFrame(actives)
df.to_csv('keep_pepset.csv', index=False)
print('Finished')