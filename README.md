# Finding related keywords using web scraping in Python and an online keyword tool for improvement in SEO 

This repository contains a python script which uses automation package Selenium and a free online keyword research instrument keywordtool.io that uses Google Autocomplete to generate hundreds of relevant long-tail keywords for any topic. It gives important fields like related keyword, search volume, cost per click (CPC) ,etc. 

The python script automates opening up the chrome browser, visiting the website keywordtool.io and entering the keywords one by one from an input file. It then clicks the search button, copies the results onto the clipboard and iteratively add these results into a final dataframe keyword by keyword.

The main aim for performing the whole activity is to derive all related keywords for a given list of keywords so that ultimately, the keywords with higher search volumes are utilised better in order to get improved SEO.

## Dependencies
* Selenium
* Pandas
* win32clipboard [ Windows Clipboard API ]
* chromedriver.exe [ Download the chromedriver executable suitable for your chrome browser from https://chromedriver.chromium.org/downloads ]


## Usage

```
python relatedkeywordswithclipboard.py
```

**Note :** Replace in the code the path of your input keywords csv file and the path of your chromedriver.exe from your local machine.
