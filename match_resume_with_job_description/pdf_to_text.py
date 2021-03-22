import pdfplumber
import os
import concurrent.futures
import time


pdf_directory = 'resume_pdf'
text_directory = 'resume_text'

# def ForLoop():
#     start = time.perf_counter()
#     for file in os.listdir(f'{pdf_directory}/'):
#         filename = os.fsdecode(file)
#         if filename.endswith('.pdf'):
#             file_name = filename.split('.')[0]
#             # print(filename)
#             all_text = '' # new line
#             with pdfplumber.open(pdf_directory+'/'+filename) as pdf:
#                 # page = pdf.pages[0] - comment out or remove line
#                 # text = page.extract_text() - comment out or remove line
#                 for pdf_page in pdf.pages:
#                    single_page_text = pdf_page.extract_text()
#                    # print( single_page_text )
#                    # separate each page's text with newline
#                    all_text = all_text + '\n' + single_page_text
#                 # print(all_text)
#                 with open(f"{text_directory}/{file_name}.txt", "w", encoding="utf-8") as file:
#                     file.write(all_text)
#
#     finish = time.perf_counter()
#     print(f'Total time ForLoop: {round(finish-start, 2)} seconds')
#                 # print(text) - comment out or remove line

class ResumeAndJD:
    def __init__(self, pdf_directory):
        self.pdf_directory = pdf_directory
        self.pdf_list = [os.fsdecode(file) for file in os.listdir(f'{self.pdf_directory}/')]

    def PdfToText(self, filename):
        if filename.endswith('.pdf'):
            file_name = filename.split('.')[0]
            # print(filename)
            all_text = ''  # new line
            with pdfplumber.open(pdf_directory + '/' + filename) as pdf:
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

    def ThreadMultiCheck(self):
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.PdfToText, self.pdf_list)
        finish = time.perf_counter()
        print(f'Total time ThreadMultiCheck: {round(finish - start, 2)} seconds')
        pass


    pass



# def pdf_to_text(filename):
#     if filename.endswith('.pdf'):
#         file_name = filename.split('.')[0]
#         # print(filename)
#         all_text = '' # new line
#         with pdfplumber.open(pdf_directory+'/'+filename) as pdf:
#             # page = pdf.pages[0] - comment out or remove line
#             # text = page.extract_text() - comment out or remove line
#             for pdf_page in pdf.pages:
#                single_page_text = pdf_page.extract_text()
#                # print( single_page_text )
#                # separate each page's text with newline
#                all_text = all_text + '\n' + single_page_text
#             # print(all_text)
#             with open(f"{text_directory}/{file_name}.txt", "w", encoding="utf-8") as file:
#                 file.write(all_text)
#
#
#
#
# def ThreadMultiCheck(b):
#     start = time.perf_counter()
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(pdf_to_text, b)
#     finish = time.perf_counter()
#     print(f'Total time ThreadMultiCheck: {round(finish-start, 2)} seconds')
#
# b = [os.fsdecode(file) for file in os.listdir(f'{pdf_directory}/')]
#
# ThreadMultiCheck(b)
