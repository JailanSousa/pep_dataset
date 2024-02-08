import biotite.sequence as seq
import biotite.sequence.align as align
from tqdm import tqdm

import pandas as pd


class SeqIdentity:
    
    def __init__(self, file):
        
        self.pepset = pd.read_csv(file, keep_default_na=False)
        
    def get_identity(self):
        
        """ Return a DataFrame of the percentage 
            identity between two sequences."""
    
        pepset = self.pepset

        # Create a subset
        fiels = ['Entry', 'pdb_code', 'Sequence', 'Keep']
        queries = pepset[fiels]
    
        # Protein substitution matrix used, which is BLOSUM62
        matrix = align.SubstitutionMatrix.std_protein_matrix()
        pident = []
    
        for query in tqdm(queries.values, desc='Identity calculation'):

            entry = query[0]
            seq1 = seq.ProteinSequence(query[2])
    
            queries = queries.drop(queries.index[0])
            for target in queries.values:
        
                etarget = target[0]
                seq2 = seq.ProteinSequence(target[2])

                # Perform an optimal alignment of two sequences based on a 
                # dynamic programming algorithm.
                alignments = align.align_optimal(seq1, seq2,
                                                  matrix, local=False)
            
                data = {
                        'Entry query': entry,
                        'Target query': etarget,
                        'Pident': align.get_sequence_identity(alignments[0],
                                                          mode='all') # Calculating identity
                        }
            
                pident.append(data)
        #df = pd.DataFrame(pident)
        #df.to_csv('pdent_tst_2.csv', index=False)
        print('done\n')
        return pd.DataFrame(pident)

    def get_high_pident(self):
        
        """ Return a list of entry sequences that 
            will be removed from the dataset."""
        
        fields = ['Entry', 'pdb_code', 'Keep']
        pset = self.pepset[fields]
        data = self.get_identity()
        identity = data[data['Pident'] >= 0.80]
        
        #Increase score for favorite peptides
        points = []
        for p in pset.values:
            pdb = p[1]
    
            if pdb:
                p[2] += 0.5
            points.append(p)
        
        # Putting high identity sequences in the same list.
        chose = []
        for i in identity.values:
            qentry = i[0]
            tentry = i[1]
            
            for p in points:
                entry = p[0]
                
                if qentry == entry:
                    q = list(p)
                    
                elif tentry == entry:
                    chose.append([q, p.tolist()])
        
        # Making decisions about which sequences will be removed from dataset.
        wins, loses, banned = [], [], []
        for c in tqdm(chose, desc='Selecting sequences'):
             
            #print(f'{c}\n')
            scoreseq1 = c[0][2]
            entrysq1 = c[0][0]
            scoreseq2 = c[1][2]
            entrysq2 = c[1][0]  
            
            if scoreseq1 == 1.5:
                if entrysq1 not in wins and entrysq1 not in loses:
                    wins.append(entrysq1)
                if entrysq2 not in loses:
                    loses.append(entrysq2)
                if entrysq2 not in banned:
                    banned.append(entrysq2)
                    
            elif scoreseq2 == 1.5:
                if entrysq2 not in wins and entrysq2 not in loses:
                    wins.append(entrysq2)
                if entrysq1 not in loses:
                    loses.append(entrysq1)
                if entrysq1 not in banned:
                    banned.append(entrysq1)
            
            elif scoreseq1 > scoreseq2:
                if entrysq1 not in banned:
                    if entrysq1 not in wins:
                        wins.append(entrysq1)
                    if entrysq2 not in loses:
                        loses.append(entrysq2)
                        
            elif scoreseq2 > scoreseq1:
                if entrysq2 not in banned:
                    if entrysq2 not in wins:
                        wins.append(entrysq2)
                    if entrysq1 not in loses:
                        loses.append(entrysq1)
            
            else:
                if scoreseq1 == scoreseq2:
                    if entrysq1 not in banned:
                        if entrysq1 not in wins and entrysq1 not in loses:
                            wins.append(entrysq1)
                        if entrysq2 not in loses:
                            loses.append(entrysq2)
        print('done\n')           
        return loses
    
    def remove_high_piden_seq(self):
        """Removing the sequences with more 
            than 80% of identity from dataset."""
            
        loses = self.get_high_pident()
        pset = self.pepset.set_index('Entry')
        
        for l in tqdm(loses, desc='Removing sequences from dataset'):
            
            pset.drop(index=l, inplace=True)
        
        pset.to_csv('remove_high_pident_tst.csv')
        
        print('done')
        
file = 'keep_pepset.csv'

pident = SeqIdentity(file)

pident.remove_high_piden_seq()
