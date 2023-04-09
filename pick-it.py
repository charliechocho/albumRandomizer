import random
import csv

filename = 'csvs/albums.csv'

def load_albums(filename):
    data1 = []
    with open(filename, 'r') as f:
        data = csv.reader(f, delimiter=';')        
        for row in data:
            data1.append(row)
        
        tot_lines = len(data1)
        
        return tot_lines, data1
        
def pick_num(num_albums):
    num = random.randint(0, num_albums)
    return num 

def pretty_print(album_pick):
    header = ['Artist', 'Album', 'Year', 'Type', 'Genre', 'None']
    for i, item in enumerate(album_pick):
        if header[i] != 'None':
            print(f"{header[i]}:\t{item}")       
        
       
num_lines, data = load_albums(filename)
no = pick_num(num_lines - 1)

print(f"Out of the current {num_lines} album, Maybe pick this one?:\t")
pretty_print(data[no])



