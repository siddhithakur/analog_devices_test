# Count the lines in various files windows system

Run pdfreadtesseract.py file
input the file directory and enter exnetion for files to be fetched

# Installations

pip install requirements.txt

## Need below installations for reading text from image converted pdfs
Refer ----> https://stackoverflow.com/questions/53481088/poppler-in-path-for-pdf2image

install poppler folder ---->  https://github.com/oschwartz10612/poppler-windows/releases/

extract zip and copy bin path 
Images = convert_from_path(Pdf_file_path, dpi=500,poppler_path='.\\Release-21.11.0-0\\poppler-21.11.0\\Library\\bin')
optional ----> set env variables -----> poppler_path = .\Release-21.11.0-0\poppler-21.11.0\Library\bin

## Install teseeract
Refer ---> https://stackoverflow.com/questions/62245083/oserror-winerror-740-the-requested-operation-requires-elevation/62278516#62278516
install latest version -- https://github.com/UB-Mannheim/tesseract/wiki
run .exe and copy the path.exe to script
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
optional env variables -----tesseract_path=C:\\Program Files\\Tesseract-OCR

