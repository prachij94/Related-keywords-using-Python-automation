# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:19:16 2018

@author: Prachi Jain
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time as t
import pandas as pd
import win32clipboard

df = pd.read_csv('C:/Users/IMART/Desktop/My_Data/new.csv')
df = df['Keywords'].tolist()

options = webdriver.ChromeOptions()
#options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--start-maximized")
options.add_argument("--test-type")
#options.add_argument("--headless")

finaldf = pd.DataFrame(columns = ['Keyword','Related Keywords'])

row=0
for i in df:
    
   driver = webdriver.Chrome(executable_path='C:/Users/IMART/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
   t.sleep(3)
   #driver = webdriver.Firefox(executable_path='C:/Users/imart/Downloads/geckodriver-v0.21.0-win64/geckodriver.exe')
   driver.get('https://keywordtool.io/google')
   # type keyword text
   text_area = driver.find_element_by_name('keyword')

   text_area.send_keys(df[i])

   # click search button
   s1 = Select(driver.find_element_by_id('edit-country-language'))
   s1.select_by_value("IN:en-IN")
   
   python_button = driver.find_element_by_id('edit-submit')
   python_button.click()

   t.sleep(20)
   # click export to csv button
   export_button = driver.find_element_by_xpath('//*[@id="edit-operations-wrapper--5"]/div/button')
   export_button.click()
   
   check=driver.find_element_by_id('edit-copy--5')
   check.click()
   win32clipboard.OpenClipboard()
   relatedkeywordsdata = win32clipboard.GetClipboardData()
   win32clipboard.CloseClipboard()
   relatedkeywordsdatalist = relatedkeywordsdata.split("\r\n")
   for j in range(0,len(relatedkeywordsdatalist)):
       finaldf.set_value(row,'Keyword',df[i])
       finaldf.set_value(row,'Related Keywords',relatedkeywordsdatalist[j])
       row = row+1
   driver.quit()
   
   
#win32clipboard.OpenClipboard()
#win32clipboard.EmptyClipboard()
#win32clipboard.SetClipboardText('testing 123')
#win32clipboard.CloseClipboard()