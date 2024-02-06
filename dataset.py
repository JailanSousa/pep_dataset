
import re
import pandas as pd

from dbsetmain import main, read_info, sequence
import os

os.chdir('/home/jssousa/neuro_pep_dataset/ncbi_dtsets')

class InsectPepDataSet:
    
    def __init__(self, file):
        
        self.info = read_info(file)
        self.content = main
    
    def taxonomy(self):
        
        info = self.content(self.info, 'ORGANISM', 'REFERENCE')
        taxonomy = []
        
        # Removing disnecessaries caracteres
        for i in info:
            
            get_org = re.sub(r'ORGANISM','', i)
        
            fix_txt = ''.join(get_org)
            taxonomy.append(fix_txt.strip())
        
        return taxonomy
    
    def version_id(self):
        
        info = self.content(self.info, 'VERSION', 'DBSOURCE')
        version_id = []
        
        for i in info:
        
            id = re.sub(r'^VERSION\s+|_[A-Z]','', i.rstrip())
            
            version_id.append(id)
        
            
        return version_id
    
    def comment(self):
        info = self.content(self.info, 'COMMENT', 'FEATURES')
        comment = []
        
        for i in info:
        
            fix_comment = re.sub(r'COMMENT','',i)
            
            text = ''.join(fix_comment)
    
            comment.append(text.strip())
        
        return comment
    
    def reference(self):
        
        info = self.info
        text = ''
        reference = []
        for i in info:
            
            index_ref = i.find('REFERENCE')
            
            index_comm = i.find('COMMENT')
            
            if index_comm != -1:
                text = i[index_ref:index_comm]
            else:
                index_feature = i.find('FEATURES')
                text = i[index_ref:index_feature]
            
                
            if re.findall(r'(?=PUBMED)\w+', text):
                
                pubmed = re.findall(r'(?=PUBMED).+', text)
                pubtext = '\n'.join(pubmed)
                reference.append(pubtext.strip())
                
            else: 
                
                journal = re.findall(r'(?<=JOURNAL).+', text)
                jourtext = ''.join(journal)
                reference.append(jourtext.strip())
        return reference
    
    def title(self):
        
        info = self.info
        text = ''
        titles = []
        
        for i in info:
            
            index_ref = i.find('REFERENCE')
            
            index_comm = i.find('COMMENT')
            
            if index_comm != -1:
                text = i[index_ref:index_comm]
            else:
                index_feature = i.find('FEATURES')
                text = i[index_ref:index_feature]
            
                
            if re.findall(r'(?=TITLE)\w+', text):
                
                title = ''.join(re.findall(r'(?=TITLE).+?(?=JOURNAL)', text, re.DOTALL))
                titles.append(title.strip())
                
            else: 
                titles.append('null')
                
        return titles
    
    def definition(self):
        
        info = self.content(self.info, 'DEFINITION', 'ACCESSION')
        
        definition = []
        for i in info:
            
            fix_definition = re.findall(r'[A-z][a-z].+', i)
            text = '\n'.join(fix_definition)
            
            definition.append(text)
            
        return definition
    
    def dbsource(self):
        
        info = self.content(self.info, 'DBSOURCE', 'KEYWORDS')
        
        source = []
        for i in info:
            
            dbs = re.findall(r'(?<=DBSOURCE).+(?<=:)|(?<=DBSOURCE).+', i)
            dbstext = ' '.join(dbs)
            
            source.append(dbstext.strip())
        
        return source
    
    def add_seq(self):
        
        file = 'paraly_peptide.fasta'
        fasta = sequence(file)
        id_seq = self.version_id()
        
        seq = []
        for i in id_seq:
            
            pep = [f[1] for f in fasta if f[0] == i]
                
            seq.append(''.join(pep))
        
        return seq
    
    def pep_lenth(self):
        
        seq = self.add_seq()
        lenth = []
        for s in seq:
            
            aa_count = sum([x.isupper() for x in s])
            
            lenth.append(aa_count)
        
        return lenth
    
    def dtset(self):
        
        pepdataset = {
            'version': self.version_id(),
            'sequence': self.add_seq(),
            'lenght': self.pep_lenth(),
            'taxonomy': self.taxonomy(),
            'dbsource': self.dbsource(),
            'definition': self.definition(),
            'reference': self.reference(),
            'title': self.title(),
            'comment': self.comment(),    
        }
        

        df = pd.DataFrame(pepdataset)
        df_non_redundante = df.drop_duplicates(subset=['sequence'], keep='first')
        return df_non_redundante.to_csv('paraly_peptide.csv', index=False)

file_name = 'paraly_peptide.gp'
tst = InsectPepDataSet(file_name)


tst.dtset()
print('OK')