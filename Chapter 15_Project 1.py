# Chapter 15
# Practice Project 1

# PDF Paranoia

import os, PyPDF2, re, pprint

def pickPdf():
     pdfFiles = []
     for foldernames, subfolders, filenames in os.walk('d:\\a\\b\\c'):
          for filename in filenames:
               if filename.endswith('.pdf') is True:
                     pdfPath = foldernames + '\\' + filename
                     pdfFiles.append(pdfPath)



def encrypt():
     for pdfFile in pdfFiles:
          os.chdir(os.path.dirname(pdfFile))
          print(os.path.basename(pdfFile))
          pdfFileObj = open(os.path.basename(pdfFile), 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
          pdfWriter = PyPDF2.PdfFileWriter()
          pdfNameStyle = re.compile(r'(.*).pdf')
          pdfName = pdfNameStyle.search(os.path.basename(pdfFile))
     
          try:
               for pdfPage in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pdfPage)
                    pdfWriter.addPage(pageObj)
          except:
               continue

          os.chdir('d:\\a\\b\\cats')
          print('Start encrypting')
          pdfWriter.encrypt('rangerover')
          resultPdf = open(pdfName.group(1) + '_Encrypted_2.pdf','wb')
          pdfWriter.write(resultPdf)
          resultPdf.close()



def testPsw():
     print('Please input a password you want to try')
     psw = input()
     pickPdf()
     print(pprint.pformat(pdfFiles))
     for pdfFile in pdfFiles:
          os.chdir(os.path.dirname(pdfFile))
          pdfFileObj = open(os.path.basename(pdfFile), 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
          if pdfReader.isEncrypted is True:
               print(os.path.basename(pdfFile))
               if pdfReader.decrypt(psw) == 0:
                    print('The password for ' + os.path.basename(pdfFile) + ' in ' + os.path.dirname(pdfFile) + ' is incorrect!')
               else:
                    print(os.path.basename(pdfFile) + ' is decrypted!')
     print('Done')
