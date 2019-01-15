import codecs
import shutil
import csv

with codecs.open("Dummy-Data-1.csv", encoding="utf-16") as input_file:
    with codecs.open(
            "Dummy-Data-8.csv", "w", encoding="utf-8") as output_file:
        shutil.copyfileobj(input_file, output_file)
		
with codecs.open('Dummy-Data-8.csv', encoding="utf-8") as input_file:
		spamreader = csv.reader(input_file, delimiter='\t')
		line_count = 0
		for row in spamreader:
			if line_count == 0:
				print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:
				print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
				line_count += 1
		print(f'Processed {line_count} lines.')