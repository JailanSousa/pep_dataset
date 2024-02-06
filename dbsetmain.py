import re

def read_info(file):
    
        with open(file, 'r') as file_obj:
            content = file_obj.read()
            
            info = [x for x in content.split('//\n\n') if x]
            
        return info

def main(info, *index):
    
    target = []
    for i in info:
        
        try:
        
            lowest_index = i.index(index[0])
            highest_index = i.index(index[1])
            text = i[lowest_index:highest_index].strip()
        
            if text:
                target.append(text)
                
            else:
                pass
            
        except ValueError:
            target.append('null')

    return target

def sequence(fasta):
    
    peptides = []
    with open(fasta, 'r') as file_obj:
        content = file_obj.read()
        
        seq = [x.rstrip() for x in content.split('>') if x]
        
        part1_id = re.compile(r'\|(.+)\|')
        part2_id = re.compile(r'^[A-Z.0-9]+(?<=\s)?')
        
        for s in seq:
            
            if part1_id.findall(s):
                
                id = part1_id.findall(s)
                
            elif part2_id.findall(s):
                
                id = part2_id.findall(s)
            
            pep = ''.join(re.findall(r'(?=\n).+', s, re.DOTALL))
            
            
            peptides.append([''.join(id), re.sub(r'\n','', pep)])
            
        return peptides
            
if __name__ == '__main__':            
    
    file = 'neurotoxic_peptide.fasta'
    tst = sequence(file)
    
    for t in tst:
        print(t)