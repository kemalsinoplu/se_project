#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = "https://www.sahibinden.com/otomobil?pagingOffset="

start_page = 0
end_page = 20

# CSV dosyasını oluştur ve başlıkları yaz
# CSV dosyasını kaydetme kısmını düzenle
csv_file = open('data.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Brand', 'Model', 'Price', 'Year', 'KM', 'City'])


for page in range(start_page, end_page + 1, 20):
    # Tarayıcıyı her sayfa için yeniden başlat
    browser = webdriver.Chrome()
    current_url = url + str(page)
    browser.get(current_url)
    time.sleep(1)

    brands = []
    brand_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsTagAttributeValue')   
    for i in range(0, len(brand_elements), 3):
        if brand_elements[i].text.strip():
            brands.append(brand_elements[i].text)

    models = []
    model_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsTagAttributeValue')
    for i in range(1, len(model_elements), 3):
        if model_elements[i].text.strip():
            models.append(model_elements[i].text) 
            
    prices = []
    price_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsPriceValue')
    for element in price_elements:
        price_text = element.text.strip()
        if price_text:
            prices.append(price_text)

    years = []
    year_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsAttributeValue')
    for i in range(0, len(year_elements), 2):
        if year_elements[i].text.strip():
            years.append(year_elements[i].text)    

    kMs = []
    km_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsAttributeValue')
    for i in range(1, len(km_elements), 2):
        if km_elements[i].text.strip():
            kMs.append(km_elements[i].text)

    citys = []
    city_elements = browser.find_elements(By.CSS_SELECTOR, 'td.searchResultsLocationValue.true')    
    for element in city_elements:
        city_text = element.text.strip()
        if city_text:
            citys.append(city_text.replace("\n", "/"))

    # Verileri ekrana yaz ve CSV dosyasına kaydet
    for brand, price, model, km, year, city in zip(brands, prices, models, kMs, years, citys):
        output = f"{brand}/{model} -- {price} -- {year} -- {km} kM -- {city}"
        print(output)  # Konsola yazdır
        csv_writer.writerow([brand, model, price, year, km, city])  # CSV'ye yaz

    # Tarayıcıyı kapat
    browser.close()

# CSV dosyasını kapat
csv_file.close()


# In[ ]:




