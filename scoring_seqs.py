import pandas as pd
from tqdm import tqdm

def scoring_seqs(file):
    
    pepset = pd.read_csv(file, keep_default_na=False)

    score = []
    for i in range(len(pepset)):
    
        if 'VGSC' in pepset.ShortFunction[i] or 'Nav' in pepset.ShortFunction[i]:
        
            if pepset.pdb_code[i] != 'null':
                score.append(1.5)
            else:
                score.append(1)
        
        else:
        
            if pepset.pdb_code[i] != 'null':
                score.append(0.5)
            else:
                score.append(0) 

    pepset['Score'] = score
    pepset.to_csv('pepset_score_tst.csv', index=False)