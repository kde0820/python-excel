import xlsxwriter

data_list = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'F']
workbook = xlsxwriter.Workbook('dropdown_test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_row('A1', ['과목', '등급'])

worksheet.write_column('D2', data_list)

worksheet.write('A2', '데이터 베이스')
worksheet.data_validation('B2', {'validate': 'list',
                                 'source': '=$D$2:$D$9'})

worksheet.write('A3', '소프트웨어 공학')
worksheet.data_validation('B3', {'validate': 'list',
                                 'source': data_list})

workbook.close()