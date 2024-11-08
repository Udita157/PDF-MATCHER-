import hashlib

def pdf_matcher(file1,file2):
    h1 = hashlib.sha1()  # Generate 2 unique keys for the pdf
    h2 = hashlib.sha1()

    with open(file1,'rb') as file: #rb= read binary//as pdf is a binary file
        chunk = 0
        while chunk != b'':  # b''=empty binary string//chunk !=empty binary string
            chunk = file.read(1024) #read 1024 bits at a time
            h1.update(chunk)

    with open(file2,'rb') as file: #rb= read binary//as pdf is a binary file
        chunk = 0
        while chunk != b'':  # b''=empty binary string//chunk !=empty binary string
            chunk = file.read(1024) #read 1024 bits at a time
            h2.update(chunk)

    return h1.hexdigest() , h2.hexdigest() #hexdigest == to convert to hexadecimal


pdf1,pdf2 = pdf_matcher('matching1.pdf' , 'matching1 - Copy.pdf')

if pdf1 == pdf2:
    print('The 2 PDFs are Identical')
else:
    print('The 2 PDFs are NOT Identical')
    
