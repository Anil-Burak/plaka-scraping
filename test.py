import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import ddddocr
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument("--headless") # Bunu sonra değiştiricez
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

ocr = ddddocr.DdddOcr(
    beta=True, 
    show_ad=False,
)

ocr.set_ranges(0)

try:
    url = "https://www.1915canakkale.com/online-islemler/ihlalli-gecis-sorgulama-ve-online-odeme"
    driver.get(url)
    time.sleep(2)
    captcha_img_element = driver.find_element(By.CLASS_NAME, "captcha")

    captcha_png = captcha_img_element.screenshot_as_png

    for _attempt in range(5):
        res = ocr.classification(captcha_png)
        if len(res) == 6:  # Captcha uzunluğu 6 karakter ise kabul et 5 kere dene
            break
        captcha_img_element.click()
        time.sleep(1)
        captcha_png = captcha_img_element.screenshot_as_png
        print(f"Okunan Captcha: {res}")
        
    print(f"Son Captcha: {res}")

    input_box = driver.find_element(By.ID, "Captcha")
    input_box.clear()
    input_box.send_keys(res)

    plaka_box = driver.find_element(By.ID, "PlateNumber")
    plaka_box.send_keys("")      #Buraya plaka yazarsın
    checkbox = driver.find_element(By.ID, "IsReadText")

    driver.execute_script("arguments[0].click();", checkbox)

    buton = driver.find_element(By.XPATH, "//button[text()='SORGULA']")
    buton.click()

    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    veriler = soup.find_all("div", class_="col-md-12")

    for veri in veriler:
        print(veri.text)

except Exception as e:
    print(f"Hata oluştu: {e}")
finally:
    driver.quit()