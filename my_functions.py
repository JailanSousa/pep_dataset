import csv

def read_csv(file):
    """Read a csv file and return a list."""
    with open(file, 'r') as f_obj:
        content = csv.reader(f_obj)
        
        header = next(content)