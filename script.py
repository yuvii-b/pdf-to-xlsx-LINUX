import PyPDF2
import csv
import camelot

pdf_file = "list.pdf"
read = PyPDF2.PdfReader(pdf_file)
pages = len(read.pages)

# pages = int(str(file)[13:].replace(">", ""))

for i in range(pages + 1):
    file = camelot.read_pdf(pdf_file, pages="{}".format(i))
    lst = file[0].df.values.tolist()
    if(i == 0):
        heading = [s.replace("\n", "") for s in file[0].df.values.tolist()[0]]
        with open('csvdata.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(heading)
    with open("csvdata.csv", "a") as f:
        writer = csv.writer(f, delimiter=',')
        for line in lst[1:len(lst)+1]:
            writer.writerow(line)
f.close()
