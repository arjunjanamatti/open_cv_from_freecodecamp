import PyPDF2
import pdfplumber
import os

pdf = pdfplumber.open('damoder.pdf')
total_pages = len(pdf.pages)
print(total_pages)
page = pdf.pages[0]
text = page.extract_text()
# print(text)
pdf.close()

for file in os.listdir('.'):
    filename = os.fsdecode(file)
    if filename.endswith('.pdf'):
        all_text = '' # new line
        with pdfplumber.open(file) as pdf:
            # page = pdf.pages[0] - comment out or remove line
            # text = page.extract_text() - comment out or remove line
            for pdf_page in pdf.pages:
               single_page_text = pdf_page.extract_text()
               print( single_page_text )
               # separate each page's text with newline
               all_text = all_text + '\n' + single_page_text
            print(all_text)
            # print(text) - comment out or remove line
