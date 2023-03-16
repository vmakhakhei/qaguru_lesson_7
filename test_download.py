import requests
import os
import zipfile

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

    path = './resourses/'
    file_dir = os.listdir(path)
    with zipfile.ZipFile('testarhive.zip', 'w') as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file)


def test_read_pdf():
    pass


def test_read_xlsx():
    pass


def test_read_csv():
    pass
