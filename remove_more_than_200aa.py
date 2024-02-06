import os
import csv
import pandas as pd

os.chdir('/home/jssousa/neuro_pep_dataset/pdb_sets')

file = 'rcsb_pdb_voltage_gated_sodium_inhibitor.csv'

with open(file, 'r') as file_obj:
    reader = csv.reader(file_obj)
    
    header = next(reader)
    
    new_file = []
    for col in reader:
        
        lenth = int(col[7])
        
        if lenth <= 200:
            
            new = {
                'Entry ID': col[0],
                'Database Name': col[4],
                'Accession Code(s)': col[5],
                'Sequence': col[6],
                'Polymer Entity Sequence Length': col[7]
            }
            
            new_file.append(new)
    
    df = pd.DataFrame(new_file)
    df.to_csv('rcsb_pdb_voltage_gated_sodium_inhibitor.csv', index=False)
    
print('OK')