import os
import PyPDF2


def print_institutional_code(file_path):
    pdfFileObject = open(file_path, 'rb')
 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    page_numbers = pdfReader.getNumPages()

    for i in range(0, page_numbers):
        pdfFileObject = open(file_path, 'rb')
 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

        pageObject = pdfReader.getPage(i)

        text = pageObject.extractText()
        institute_no = ""
        no = ""
        found = False
        nums = '0123456789'

        for t in text:
            if t == "#":
                found = True
            if(found == True):
                institute_no += t
                if len(institute_no) >= 7:
                    found = False
                    break

        institute_no = institute_no[3:]
        for n in institute_no:
            if n in nums:
                no += n
        
        if len(no) > 0:
            print(no)
        pdfFileObject.close()


def move_all_ext(extension, source_root):
    # Recursively walk source_root
    for (dirpath, dirnames, filenames) in os.walk(source_root):
        # Loop through the files in current dirpath
        for filename in filenames:
            # Check file extension
            if os.path.splitext(filename)[-1] == extension:
                # Move file
                # print(filename)
                # print(dirpath)
                file_path = dirpath + "/" + filename
                print_institutional_code(file_path)


move_all_ext(".pdf", "E:\\projects/python/pdf_extractor/")