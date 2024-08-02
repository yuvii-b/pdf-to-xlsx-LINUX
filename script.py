import csv
import camelot

heading = [] # The row heading of the tablular data in the pdf data is given here as a list of strings
with open('csvdata.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(heading)

starting_page = 1 # Denotes the first page, page from which the table in pdf is to be converted into csv(xls)
ending_page = 2 # Denotes the last page, page upto which the table in pdf is to be converted into csv(xls)
pdf_file = '' # The name or path(if the file if not in the same directory) of the pdf is to be given here
for i in range(starting_page, ending_page + 1):
    file = camelot.read_pdf(pdf_file, pages="{}".format(i))
    lst = file[0].df.values.tolist()
    with open('csvdata.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        for line in lst[1:len(lst) + 1]:
            writer.writerow(line)
f.close()
