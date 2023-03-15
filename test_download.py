import requests
import os
import zipfile

def test_download_xlsx():
    url = 'https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_XLSX.xlsx'
    response = requests.get(url, allow_redirects=True)

    with open('Free_Test_Data_100KB_XLSX.xlsx', 'wb') as file_xlsx:
        file_xlsx.write(response.content)

def test_download_pdf():
    url = 'https://www.orimi.com/pdf-test.pdf'
    response = requests.get(url)

    with open('pdf-test.pdf', 'wb') as file_pdf:
        file_pdf.write(response.content)

def test_download_csv():
    url = 'https://sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'
    response = requests.get(url)

    with open('Sample-Spreadsheet-100-rows.csv', 'wb') as file_csv:
        file_csv.write(response.content)

def test_archivate():
