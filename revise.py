file = 'insecticidal_peptides.gp'

with open(file, 'r') as file_obj:
    #lines = file_obj.readlines()
    contents = file_obj.read()
    
    info = [x.rstrip() for x in contents.split('//\n\n') if x]

    
    for i in info:
        if '7WKF' in str(info):
            print('True')
