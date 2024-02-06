import pandas as pd
import os
import csv

#os.chdir('/home/jssousa/neuro_pep_dataset/ncbi_dtsets')

def add_taxon(file):
    
    with open(file, 'r') as f_obj:
        reader = csv.reader(f_obj)
    
        header = next(reader)
    
        kingdoms = ['Bacteria', 'Metazoa', 'Viruses', 
                    'Fungi', 'Viridiplantae']
    
        new_file = []
        for r in reader:
            taxonomy = r[3].split('\n')
        
            organism = taxonomy[0]
        
            taxons = [x for x in kingdoms if x in str(taxonomy)]
        
            if not [x[0] for x in taxons]:
                taxons.append('synthetic')
        
            kingdom = taxons[0]
        
            new_set = {
                'Entry': r[0],
                'Sequence': r[1],
                'Lenth': r[2],
                'Kingdom': kingdom,
                'Organism': organism,
                'DBsource': r[4],
                'Definition': r[5],
                'PMD_ID': r[6],
                'Title': r[7],
                'Function': r[8]
            }
        
            new_file.append(new_set)
        
        df = pd.DataFrame(new_file)
        return df.to_csv('ncbi_allsets.csv', index=False)


def del_tax(file):
    
    with open(file, 'r') as f_obj:
        reader = csv.reader(f_obj)
    
        header = next(reader)
    
        kingdoms = ['Bacteria', 'Archaea', 'Metazoa',
                    'Viruses', 'Fungi', 'Viridiplantae', 'unknown']
    
        new_file = []
        check = ''
        for r in reader:
            
            for k in kingdoms:
                
                if k in r[3]:
                    kingdom = k
                    check = True
                
                elif k is 'unknown':
                    
                    check = False
                
                elif check is False:
                    kingdom = k
                    check = True
                    
    
            new_set = {
                'Entry': r[0],
                'Sequence': r[1],
                'Lenth': r[2],
                'Kingdom': kingdom,
                'Organism': r[4],
                'DBsource': r[5],
                'Definition': r[6],
                'PMD_ID': r[7],
                'Title': r[8],
                'Function': r[9]
            }
        
            new_file.append(new_set)
            
    
        df = pd.DataFrame(new_file)
        return df.to_csv('uniprot_add_kingdom.csv', index=False)
            

file = 'uniprot_add_kingdom.csv'

del_tax(file)   
print('OK')