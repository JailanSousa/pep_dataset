import re
import pandas as pd

def p_fasta(file):
    
    with open(file, 'r') as f_obj:
    
        fastas = f_obj.read()
    
        fasta = [x for x in fastas.split('>') if x]
    
        dtset = []
        for f in fasta:
        
            #entry = re.findall(r'(?<=as:).+?(?=\|)|(?<=as:).+?(?<=\s)', f.strip())
            entry = re.findall(r'(?<=\|sp|gb:).+?(?<=\s)', f.strip())
            
             
            if entry:
                seq = ''.join(re.findall(r'(?=\n).+', f, re.DOTALL))
                
                #organism = ' '.join(re.findall(r'\b[A-Z][a-z]+?\b', f.strip()))
                #genera = ' '.join(re.findall(r'(?<=spider).+(\b[A-Z][a-z]+?\b)', f.strip(), re.DOTALL))
                #pattern = r'(?='+genera+').+?(?=\n)'
                #specie = ''.join(re.findall(pattern, f, re.DOTALL))
                comment = ''.join(re.findall(r'(?<=spider).+[a-z]', f, re.DOTALL))
                
                
                dtset.append([''.join(entry), re.sub(r'\n', '', seq), comment])
            
        return dtset
    

def seq_lenth(p_fasta):
    
    pep = []
    for f in p_fasta:
    
        lenth = sum([x.isupper() for x in f[1]])
        
    
        fastas = {
            'Definition': f[0],
            'Sequence': f[1],
            'Organism': f[2],
            'Lenth': lenth
        }
        
        pep.append(fastas)
    
    df = pd.DataFrame(pep)
    return df.to_csv('arcnoserver_all_neuro_pep.csv', index=False)


file = '/home/jssousa/neuro_pep_dataset/arachnoserve_dtsets/arach_neurotoxin.fasta'
tst = seq_lenth(p_fasta(file))

print('OK')