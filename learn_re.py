# Learn regular expression in python
# mata caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | = OU
# . = Qualquer caracter (com exeção da quebra de linha)
# [] = um conjunto de caracteres
# QUANTIFICADORES
# * = 
# + =
# ? = 
# { } = 

import re
from pprint import pprint

file_name = 'sample_tst.gp'

with open(file_name) as file_obj:
    content = file_obj.read()
    
    lines = content.split('//')
    
    comment, version, taxonomy, reference, definition, db_source = [], [], [], [], [], []
    
    
    for line in lines:
        
        # GET TAXONOMY
        organism_index = line.find('ORGANISM')
        reference_index = line.find('REFERENCE')
        
        get_org = re.findall(r'\b[A-z][a-z]*\b', line[organism_index:reference_index])
        
        get_org = line[organism_index:reference_index]
        fix_org = re.findall(r'\b[A-z][a-z]*\b', get_org)
        org_string = ' '.join(fix_org)
        
        taxonomy.append(org_string)
   
        # GET VERVION ID
        version_index = line.find('VERSION')
        gi_index = line.find('GI')
        
        fix_version = re.sub(r'^VERSION\s+','', line[version_index:gi_index])
        fix_version = line[version_index:gi_index].strip()
        
        version.append(fix_version.rstrip())
      
        # GET COMMENT CONTENT
        comment_index = line.find('COMMENT')
        feature_index = line.find('FEATURES')
        
        text = line[comment_index:feature_index]#.split('            ')
        minin_txt = re.findall(r'\b[A-z][a-z]*\b', text)
        text_fixed = ' '.join(minin_txt)
    
        comment.append(text_fixed)
        
        # GET DEFINITION
        
        def_index = line.find('DEFINITION')
        acc_index = line.find('ACCESSION')
        
        def_txt = line[def_index:acc_index].rstrip()
        
        fix_definition = re.findall(r'[A-z][a-z].+', def_txt,)
        #fix_definition = re.findall(r'(?<==).+?(?=;)', def_txt)
        #fix_definition = re.findall(r'\b[A-z][a-z]+\b', def_txt)
        txt_def = ' '.join(fix_definition) 
        
        definition.append(txt_def)
        
        
        # GET REFERNECE
        
      
        ref_index = line.find('REFERENCE')
        
        comm_index = line.find('COMMENT')
        
        #fea_index = line.find('FEATURES')
        
        if comment_index != -1:
            ref_text = line[ref_index:comment_index]
                
        else:
            fea_index = line.find('FEATURES')
            ref_text = line[ref_index:feature_index]
        
        #reference.append(pub)
        
        # GET DBSOURCE
        
        source_index = line.find('DBSOURCE')
        keywrs_index = line.find('KEYWORDS')
        
        db_source. append(line[source_index:keywrs_index].rstrip())
    
    
    
    
    for i in comment:
        pprint(i)