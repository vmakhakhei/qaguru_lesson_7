import PyPDF2
import openpyxl
import os
import requests
import zipfile

pdf_url = 'https://www.orimi.com/pdf-test.pdf'
xlsx_url = 'https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_XLSX.xlsx'

pdf_filename = os.path.basename(pdf_url)
xlsx_filename = os.path.basename(xlsx_url)


def test_download():
    response = requests.get(xlsx_url)
    with open(f"resourses/{xlsx_filename}", "wb") as file_xlsx:
        file_xlsx.write(response.content)

    response = requests.get(pdf_url)
    with open(f"resourses/{pdf_filename}", "wb") as file_pdf:
        file_pdf.write(response.content)


def test_acrivate_files_to_zip():
    try:
        os.mkdir('resourses')
    except:
        print('resourses уже создана')

    path = './resourses'
    with zipfile.ZipFile('testarhive.zip', 'w') as zf:
        zf.write(f'{path}/{pdf_filename}', 'pdf_filename.pdf')
        zf.write(f'{path}/username.csv', 'csv_filename.csv')
        zf.write(f'{path}/{xlsx_filename}', 'xlsx_filename.xlsx')


def test_read_pdf():
    with zipfile.ZipFile('testarhive.zip') as zf:
        with zf.open('pdf_filename.pdf', 'r') as open_zf:
            reader = PyPDF2.PdfReader(open_zf)
            number_of_pages = len(reader.pages)
            assert number_of_pages == 1
            text = reader.pages[0].extract_text()
            assert 'PDF Test File' in text, "Haven't text or file to read"


def test_read_xlsx():
    with zipfile.ZipFile('testarhive.zip') as zf:
        with zf.open('xlsx_filename.xlsx', 'r') as open_zf:
            book = openpyxl.load_workbook(open_zf)
            sheet = book.active
            assert 'SR.' in sheet['A1'].value
            assert 'NAME' in sheet['B1'].value
            assert 'GENDER' in sheet['C1'].value


def test_read_csv():
    with zipfile.ZipFile('testarhive.zip') as zf:
        with zf.open('csv_filename.csv', 'r') as csvfile:
            count_row = 0
            for _ in csvfile:
                count_row += 1
            assert 6 == count_row
