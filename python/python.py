import xlwt

if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表sheet
    # 往表中写内容,第一各参数 行,第二个参数列,第三个参数内容
    worksheet.write(0, 0, 'hello world')
    worksheet.write(0, 1, '你好')
    workbook.save('first.xls')  # 保存表为students.xls
