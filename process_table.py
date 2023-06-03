"""
" Table info Processor
"""
import re
import copy
from selenium import webdriver
from selenium.webdriver.common.by import By


class TableProcessor:
    def readLine(self, table)->list:
        out = []
        for col in table.find_elements(By.TAG_NAME, "td"):
            out.append(col.text)
        return out
    def readTable(self, table)->list:
        out = []
        for line in table.find_elements(By.TAG_NAME, "tr"):
            out.append(self.readLine(line))
        return out

    def read(self, driver:webdriver)->list:
        out = []
        for table in driver.find_elements(By.TAG_NAME, "table"):
            out.append(self.readTable(table))
        return out
    def __init__(self):
        self._data = {}
