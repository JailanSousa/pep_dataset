import biotite.sequence as seq
import biotite.sequence.align as align

import numpy as np
import pandas as pd

from tqdm import tqdm

class SeqIdentity:
    
    """Return a dataset with amino acid sequence identity below 80%"""
    
    def __init__(self, file):
        
        self.pepset = pd.read_csv(file)
        
    def get_identity(self):
        
        """ Return a ndarray with percentage 
            identity between two sequences."""

        # Get amino acid sequences
        seqs = self.pepset.Sequence
        
        # Creating a identity matrix
        identity_matrix = np.zeros((len(seqs), len(seqs)))

        # Protein substitution matrix used, which is BLOSUM62
        matrix = align.SubstitutionMatrix.std_protein_matrix()

        # Calculating identity between sequences
        for i in tqdm(range(len(seqs)), desc='Calculating identity'):
            for j in range(len(seqs)):
                
                if i != j:
                    seq1 = seq.ProteinSequence(seqs[i])
                    seq2 = seq.ProteinSequence(seqs[j])

                    # Perform an optimal alignment of two sequences based on a 
                    # dynamic programming algorithm.
                    alignment = align.align_optimal(seq1, seq2, matrix, local=False)
                    identity = align.get_sequence_identity(alignment[0], mode='all')
                    identity_matrix[i, j] = identity
        
        print('Done!')
        return identity_matrix

    def get_redundant_seqs(self, identity_threshold=0.80):
        
        """Return a list with redundats sequences at 
            identiry threshold cutoff"""
        
        # Define sequences that must keep in the dataset
        priority = self.pepset.Keep
        identity_matrix = self.get_identity()
        
        # Finding sequences with identity above threshold
        redundant_seqs = []
        for i in range(len(identity_matrix)):
            
            for j in range(i+ 1, len(identity_matrix)):
        
                if identity_matrix[i, j] >= identity_threshold:
            
                    if priority[i] == priority[j]:
                        if i not in redundant_seqs:
                            redundant_seqs.append(j)
            
                    elif priority[i] > priority[j]:
                        if i not in redundant_seqs:
                            redundant_seqs.append(j)
            
                    else:
                        if j not in redundant_seqs:
                            redundant_seqs.append(i)
        return redundant_seqs
    
    def remove_redundants_seqs(self):
        
        """Return a csv file with non-redundat sequences at
            trheshold cutoff."""
            
        pepset = self.pepset
        redundant_seqs = self.get_redundant_seqs()

        # Removing redundat sequences
        unique_seqs = [i for i in range(len(pepset)) if i not in redundant_seqs]

        # Create uniq dataset.
        uniq = pepset.iloc[unique_seqs]
        uniq.to_csv('uniq_pepset.csv', index=False)

file = 'high_identity_tst.csv'
pident = SeqIdentity(file)

pident.remove_redundants_seqs()

