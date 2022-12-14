

from glob import glob

filename = 'train.tsv'

with open(filename, 'a') as singleFile:
    first_tsv = True
    for tsv in glob('*.tsv'):
        if tsv == filename:
            pass
        else:
            header = True
            for line in open(tsv, 'r'):
                if first_tsv and header:
                    singleFile.write(line)
                    first_tsv = False
                    header = False
                elif header:
                    header = False
                else:
                    singleFile.write(line)
    singleFile.close()