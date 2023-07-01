import pandas

file = open('dados-populacionais', 'r')

excel_data_df = pandas.read_excel(file, sheet_name='dados-populacionais.xlsx')

print(excel_data_df)