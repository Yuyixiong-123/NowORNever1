import openpyxl

wb=openpyxl.load_workbook('时间规划表.xlsx')
sheet=wb['Sheet1']
for i in range(7,24):
     cellName='B'+str(i-4)
     sheet[cellName]=str(i)+':00-'+str(i+1)+':00'
wb.save('时间规划表.xlsx')
print(1)
                    
