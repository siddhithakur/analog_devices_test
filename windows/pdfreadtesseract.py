
import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import docx2txt
import win32com.client
from tika import parser as p
import tika
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#
# def process_image(iamge_name, lang_code):
#     c = 0
#     text = pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)
#     print(text)
#     for i in text:
#         if i == "\n":
#             c += 1
#     return (c)
    
# def process_word(file_path, ext, f_format):
#     #if ext == ".docx":
#     c = 0
#     #print(file_path,ext)
#
#     if ext == ".doc" and f_format == ".doc":
#         wrd= win32com.client.Dispatch("Word.Application")
#         wrd.visible = 0
#         wb = wrd.Documents.Open(r'"'+file_path+'"')
#         wb.SaveAs(r'"'+file_path[:file_path.index(".")]+'.docx"', FileFormat = 16)
#         wb.Close()
#         wrd.Quit()
#         text = docx2txt.process(file_path[:file_path.index(".")]+'.docx')
#         for i in text:
#             if i == "\n":
#                 c += 1
#     elif ext == '.docx' and f_format == ".docx":
#         text = docx2txt.process(file_path)
#         # print(text)
#         for i in text:
#             if i == "\n":
#                 c += 1
#     return (c)
    
def process_image_pdf(path):
    Pdf_file_path = path #your file path
    Images = convert_from_path(Pdf_file_path, dpi=500,poppler_path='D:\\Test\\analog devices\\Release-21.11.0-0\\poppler-21.11.0\\Library\\bin')
    c=0
    Counter=1
    for page in Images:

        idx= "image_"+str(Counter)+".jpg" ##or ".png"
        page.save(idx, 'JPEG')
        Counter = Counter+1
    #print(Counter)
    file=Counter
    
    for i in range(1,file):
        idx= "image_"+str(i)+".jpg" ##or ".png"
        text=str(pytesseract.image_to_string(Image.open(idx)))
        c += len(text.split("\n"))

    return(c)

def process_docs(file_path):
    results = p.from_file(file_path)
    if results['content']:
        a = (results['content'].strip())
        return (len([i for i in a.split("\n")]))
    else:
        return None

def traverse(directory, file_format='.txt'):
    no_of_files = 0
    total_lines = 0
    for path, subdirs, files in os.walk(directory):

        try:
            for name in files:
                # print(name)

                with open(os.path.join(path, name)) as fp:

                    if file_format in [".txt",""] and fp.name.endswith(".txt"):
                        #print("In text if")
                        count=len(fp.readlines())
                        print("Count of lines in file = "+name, count)
                        no_of_files+=1
                        total_lines+=count
                    elif (file_format in ['.jpg','.png','jpeg','.JPG','.JPEG','.PNG'] and\
                            fp.name[fp.name.index("."):] in ['.jpg','.png','jpeg','.JPG','.JPEG','.PNG']) or \
                            (file_format in ['.doc','.docx','.DOC','.DOCX'] and
                            fp.name[fp.name.index("."):] in ['.doc','.docx','.DOC','.DOCX']) or \
                            file_format in ['.pdf'] and \
                            fp.name[fp.name.index("."):] in ['.pdf', '.PDF']:
                        count=process_docs(os.path.join(path, name))
                        if count is not None:
                            no_of_files += 1
                            total_lines += count
                            print(name,count)
                        elif file_format in ['.pdf'] and \
                                fp.name[fp.name.index("."):] in ['.pdf', '.PDF']:
                            print(os.path.join(path, name))
                            count = process_image_pdf(os.path.join(path, name))
                            print(count)
                            no_of_files += 1
                            total_lines += count
                    else:
                        continue

        except Exception as e:
            print(e)
    print("Number of files found : ", no_of_files)
    print("Total number of lines :", total_lines)
    if no_of_files>0:
        print("Average lines per file : ", total_lines/no_of_files)
    else:
        print("Average lines per file : 0")
                

directory = input("Enter thr directory to traverse = ")
file_format = input("Enter the format to be extracted = ")
traverse(directory, file_format)































