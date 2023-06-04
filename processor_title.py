"""
" Table info Processor
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class TitleProcessor:
    def read(self, driver:webdriver)->list:
        out = []
        for title in driver.find_elements(By.TAG_NAME, "title"):
            out.append(title.text)
        return out
    def __init__(self):
        self._data = {}
