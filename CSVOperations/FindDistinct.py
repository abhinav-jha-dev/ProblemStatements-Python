import csv

# Source directory path to put your csv files.
baseDirectory = "CSVOperations/Sources/"

file1 = [line.strip() for line in open(baseDirectory + 'File1.csv')]
file2 = [line.strip() for line in open(baseDirectory + 'File2.csv')]

with open('output_File.csv', 'w') as f:
    # for line in file1:
    #     if not line.split(',')[0] in file2:
    #         f.write(line + '\n')
    f.writelines('\n'.join(filter(lambda l: not l.split(',')[0] in file2, file1)))