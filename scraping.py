from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

#page1
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = 'https://web-kanji.com/search/osaka'
driver.get(url)
elems_companies_name = driver.find_elements_by_class_name('companies-item-name')
elems_companies_address = driver.find_elements_by_class_name('companies-item-address')
elems_companies_introduction = driver.find_elements_by_class_name('companies-item-introduction')

# for name,address,introduction in zip(elems_companies_name,elems_companies_address,elems_companies_introduction):
#     data = [name.text, address.text, introduction.text]
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.get("https://www.google.com/")
#     search = driver.find_element_by_name("q")
#     search.send_keys(data[0])
#     search.submit()
#     elems_a = driver.find_elements_by_tag_name('a')
#     a = elems_a[30].get_attribute("href")
#     push_data = [name.text, a, address.text, introduction.text]
#     SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     SERVICE_ACCOUNT_FILE ='scraping-for-osaka.json'
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
#     gs = gspread.authorize(credentials)
#     SPREADSHEET_KEY = '1qltRbn3z55lsHmhfFtBwsAcAkH8_PYpOPKuFPtUCN78'
#     workbook = gs.open_by_key(SPREADSHEET_KEY)
#     worksheet = workbook.worksheet("シート1")
#     worksheet.append_row(push_data)
#     time.sleep(20)

#page2-
for i in range(3,34):
    url = 'https://web-kanji.com/search/osaka/page/' + str(i)
    driver.get(url)
    elems_companies_name = driver.find_elements_by_class_name('companies-item-name')
    elems_companies_address = driver.find_elements_by_class_name('companies-item-address')
    elems_companies_introduction = driver.find_elements_by_class_name('companies-item-introduction')

    for name,address,introduction in zip(elems_companies_name,elems_companies_address,elems_companies_introduction):
        data = [name.text, address.text, introduction.text]
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://www.google.com/")
        search = driver.find_element_by_name("q")
        search.send_keys(data[0])
        search.submit()
        elems_a = driver.find_elements_by_tag_name('a')
        a = elems_a[30].get_attribute("href")
        push_data = [name.text, a, address.text, introduction.text]
        SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        SERVICE_ACCOUNT_FILE ='scraping-for-osaka.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
        gs = gspread.authorize(credentials)
        SPREADSHEET_KEY = '1qltRbn3z55lsHmhfFtBwsAcAkH8_PYpOPKuFPtUCN78'
        workbook = gs.open_by_key(SPREADSHEET_KEY)
        worksheet = workbook.worksheet("シート1")
        worksheet.append_row(push_data)
        time.sleep(20)