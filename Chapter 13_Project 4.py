# Chapter 13
# Practice Project 4

# Text Files to Spreadsheet
# In this project, I have two txt files to copy to one Excel file.

import openpyxl

def txtToExcel():

     wb = openpyxl.Workbook()

     sheet = wb.active

     file1 = open('Text1.txt').readlines()
     file2 = open('Text2.txt').readlines()
     file = [file1] + [file2]

     for columnNum in range(0,len(file)):
          for rowNum in range(0,max(len(file1),len(file2))):
               if rowNum <= len(file[columnNum]) - 1:
                    copy = file[columnNum][rowNum]
                    sheet.cell(row = rowNum + 1, column = columnNum + 1).value = copy

     wb.save('txtToExcel.xlsx')
     print('Done')
