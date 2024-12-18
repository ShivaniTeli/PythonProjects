import PyPDF3

pdfiles = ["1.pdf", "2.pdf"]
merger = PyPDF3.PdfFileMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF3.PdfFileReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')