import PyPDF2
import pdfplumber
import os


pdf_directory = 'resume_pdf'
text_directory = 'resume_text'

for file in os.listdir(f'{pdf_directory}/'):
    filename = os.fsdecode(file)
    if filename.endswith('.pdf'):
        file_name = filename.split('.')[0]
        print(filename)
        all_text = '' # new line
        with pdfplumber.open(pdf_directory+'/'+filename) as pdf:
            # page = pdf.pages[0] - comment out or remove line
            # text = page.extract_text() - comment out or remove line
            for pdf_page in pdf.pages:
               single_page_text = pdf_page.extract_text()
               # print( single_page_text )
               # separate each page's text with newline
               all_text = all_text + '\n' + single_page_text
            # print(all_text)
            with open(f"{text_directory}/{file_name}.txt", "w", encoding="utf-8") as file:
                file.write(all_text)
            # print(text) - comment out or remove line
