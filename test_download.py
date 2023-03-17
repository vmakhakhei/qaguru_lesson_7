import requests
import os
import zipfile
from PyPDF2 import PdfReader

pdf_url = 'https://www.orimi.com/pdf-test.pdf'
xlsx_url = 'https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_XLSX.xlsx'
csv_url = 'https://sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'

pdf_filename = os.path.basename(pdf_url)
xlsx_filename = os.path.basename(xlsx_url)
csv_filename = os.path.basename(csv_url)


def test_download():
    response = requests.get(xlsx_url)
    with open(f"resourses/{xlsx_filename}", "wb") as file_xlsx:
        file_xlsx.write(response.content)

    response = requests.get(pdf_url)
    with open(f"resourses/{pdf_filename}", "wb") as file_pdf:
        file_pdf.write(response.content)

    response = requests.get(csv_url)
    with open(f"resourses/{csv_filename}", "wb") as file_csv:
        file_csv.write(response.content)


def test_acrivate_files_to_zip():
    try:
        os.mkdir('resourses')
    except:
        print('resourses уже создана')

    path = './resourses'
    with zipfile.ZipFile('testarhive.zip', 'w') as zf:
        zf.write(f'{path}/{pdf_filename}', 'pdf_filename.pdf')
        zf.write(f'{path}/{csv_filename}', 'csv_filename.csv')
        zf.write(f'{path}/{xlsx_filename}', 'xlsx_filename.xlsx')


def test_read_pdf():
    with zipfile.ZipFile('testarhive.zip') as zf:
        reader = PdfReader(zf.read('pdf_filename.pdf'))
        number_of_pages = len(reader.pages)
        assert number_of_pages == 1



def test_read_xlsx():

    file = 'xlsx_filename.xlsx'
    pass


def test_read_csv():

    file = 'csv_filename.xlsx'
    pass
