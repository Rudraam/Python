# in this program we will use the pypdf module to manupilate our pdf files
from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()

# Add pdfs to merge
#In the square brackets you can add the path to your pdf files
for file in ["pdfs/Critical Thinking Essay - Fall 2023 (2).pdf","pdfs/Digital-Licence-11460274.pdf","pdfs/PHOTO dharm.pdf","pdfs/Rudramani Dhiman new Resume pdf.pdf","pdfs/Study Permit.PDF"]:
    reader = PdfReader(file) #files read
    for page in reader.pages:
        writer.add_page(page) #add pages to writer


#save the merged pdf
with open("merged.pdf","wb") as output:
    writer.write(output) #save the pdf to a file