import xlsxwriter

data_list = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'F']
workbook = xlsxwriter.Workbook('./excel/dropdown_test.xlsx')
worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

worksheet2.write_column('A1', data_list)
worksheet2.hide()

worksheet.set_column('A:A', 15)
worksheet.write_row('A1', ['과목', '등급'])

worksheet.write('A2', '데이터 베이스')
worksheet.data_validation('B2', {'validate': 'list',
                                 'source': '=Sheet2!$A$1:$A$7'})

worksheet.write('A3', '소프트웨어 공학')
worksheet.data_validation('B3', {'validate': 'list',
                                 'source': data_list})

workbook.close()